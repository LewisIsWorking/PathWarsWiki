# Arctis Nova 7 Gen 2 not detected by Windows

Written for a SteelSeries Arctis Nova 7 Gen 2, but nothing below is specific to it. The same
diagnosis applies to any USB or wireless headset that its vendor app can see and Windows cannot.

> The short version.
>> If your headset shows up in its own vendor app (SteelSeries GG, iCUE, Logitech G Hub) but
>> Windows says there is no audio device, check the **Windows Audio service** before you touch
>> a single driver. Nine times out of ten the hardware is completely fine.

## The symptom

A wireless USB headset behaves like this:

- The vendor app sees it, shows the battery level, lets you change settings.
- The same headset works perfectly over Bluetooth on a phone or a Mac.
- Windows shows no audio device, or the headset is simply absent from the Sound settings list.

That combination looks like a broken dongle or a driver problem. It usually is not.

## Why it looks like hardware but is not

Windows audio is **two** services, not one, and they fail independently.

| Service | Job | What sees it |
|---|---|---|
| `AudioEndpointBuilder` | Discovers audio endpoints and registers them with Plug and Play | Vendor apps, Device Manager |
| `audiosrv` (Windows Audio) | Owns the actual render and capture graph | The volume flyout, Sound settings, every app that plays sound |

Vendor apps talk to the USB device and to `AudioEndpointBuilder`. Both of those sit **below**
`audiosrv`. So if `audiosrv` alone is stopped, you get exactly this picture: the endpoint exists
and is healthy, the vendor app is happy, and Windows reports nothing.

The general principle is worth keeping: **find the lowest layer that still reports healthy, then
look at exactly one layer above it.** Here the device layer is fine, so the fault is in the
service layer, not in drivers or firmware.

## Diagnosis

Open PowerShell (a normal window is enough to look) and run:

```powershell
Get-Service audiosrv,AudioEndpointBuilder | Select-Object Name,Status,StartType
Get-PnpDevice -Class MEDIA,AudioEndpoint | Where-Object Status -eq 'OK' | Select-Object FriendlyName
```

### Reading the result

You are looking for this specific contradiction:

- Your headset **is** listed by `Get-PnpDevice` with `Status : OK`, both a Headphones entry and a Microphone entry.
- `audiosrv` says `Stopped`.

That is the diagnosis. The endpoints are registered and healthy, the service that plays through
them is dead.

For a bit more certainty, ask why it stopped:

```powershell
sc.exe query audiosrv
```

Check `SERVICE_EXIT_CODE`. A value of **0** means a clean stop, so nothing crashed and something
switched it off deliberately. A nonzero code, or matching events with id 7031 or 7034 in the
System log, would mean an actual fault and a different investigation.

## The fix

This needs an **administrator** PowerShell. A normal window can read the service state but cannot
start it, and you will get "Cannot open 'audiosrv' service on computer '.'" if you try.

```powershell
Set-Service audiosrv -StartupType Automatic
Start-Service audiosrv
Get-Service audiosrv
```

Sound comes back immediately. No reboot, no reinstall, no re-pairing.

## Verifying it actually worked

Do not trust the service status alone. Confirm the audio engine process is alive:

```powershell
Get-Process audiodg
```

`audiodg` is the audio device graph isolation process. It only exists while `audiosrv` is genuinely
running, so its presence is real proof rather than a status flag.

## What not to bother doing

These are the tempting dead ends, and they all cost time:

- **Reinstalling the vendor software.** It could already see the headset, so it was never the problem.
- **Re-pairing the dongle, or trying every USB port.** Port roulette just leaves stale ghost
  endpoints behind, which show up later as duplicates like `Microphone (2- Your Headset)`. Pick one
  port and stay on it.
- **Ripping out leftover virtual audio drivers.** Old motherboard audio suites (Sonic Studio,
  Nahimic and friends) often leave a virtual mixer driver behind after the app is uninstalled, and it
  looks like a prime suspect. Check first: if its endpoints show `Unknown` rather than `OK`, it is
  dormant and it is not your culprit. Do not remove a driver on a hunch.

## If it keeps happening

Something stopped the service on purpose, and the usual suspects are "gaming optimiser" or debloat
tools that disable services to save resources. Windows 11 does not log service state changes by
default, so there may be no history to inspect.

To catch it next time, enable Service Control Manager state-change logging and then watch for
event id **7036** in the System log:

```powershell
wevtutil sl System /e:true
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7036} |
    Where-Object { $_.Message -match 'Windows Audio' } |
    Select-Object TimeCreated,Message -First 20
```

If a specific tool turns out to be responsible, stopping that tool from managing services is the
real fix, rather than restarting the audio service every time.
