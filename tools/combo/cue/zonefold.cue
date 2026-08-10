// ATTEMPT at R9, zone tracking, in CUE.
//
// Pkl does this in three lines with `fold`. CUE has no fold, and structs cannot be UPDATED by
// unification (`acc & {x: "field"}` fails when acc already has x: "deck", because unification
// intersects rather than overwrites). So every "update" has to REBUILD the whole struct,
// copying all keys except the one being changed, and the fold itself has to be a recursive
// definition that re-instantiates itself for the tail of the list.
package crystron

import "list"

_extraKinds: ["synchro", "xyz", "link"]

// FINDING 3: moving the MATERIALS as well as the acting card needs a SECOND recursive fold nested
// inside the first, because each material is another whole-struct rebuild. Pkl expresses both
// folds as one line each. This is the point where the CUE version stopped being maintainable.
// Hidden (underscore) fields do not survive definition instantiation via `&` the way regular
// fields do, which silently broke the recursion. Regular field names instead.
#MoveMats: {
	mats: [...string]
	zone: string
	acc: [string]: string
	out: [string]: string

	if len(mats) == 0 {
		out: acc
	}
	if len(mats) > 0 {
		let m = mats[0]
		let upd = {
			for k, v in acc if k != m {(k): v}
			(m): zone
		}
		out: (#MoveMats & {mats: list.Drop(mats, 1), "zone": zone, acc: upd}).out
	}
}

// Recursive fold. `out` is the zone map after applying every step in `_steps` to `_acc`.
#ZoneFold: {
	inSteps: [...#Step]
	acc: [string]: string
	out: [string]: string

	if len(inSteps) == 0 {
		out: acc
	}
	if len(inSteps) > 0 {
		let s = inSteps[0]
		// Rebuild the map: every key except this card, then this card at its new zone.
		let moved = {
			for k, v in acc if k != s.card {(k): v}
			(s.card): [if s.to != "" {s.to}, acc[s.card]][0]
		}
		let withMats = (#MoveMats & {
			mats: s.materials
			zone: [if s.action == "xyz" {"attached"}, "gy"][0]
			acc:  moved
		}).out
		out: (#ZoneFold & {inSteps: list.Drop(inSteps, 1), acc: withMats}).out
	}
}

// FINDING 1: `#Route & { ... }` cannot see `steps`, `opening` or `_deck` from #Route, because CUE
// resolves references LEXICALLY rather than against the unified result. So the zone logic cannot be
// bolted on as a separate definition the way Pkl's subclassing would allow; it has to be moved
// bodily inside #Route. See combo.cue, which is where it now lives.
