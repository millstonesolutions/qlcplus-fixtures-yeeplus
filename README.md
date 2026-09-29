# QLC+ fixture profiles — YeeSite

[QLC+](https://www.qlcplus.org/) 4 fixture definitions for YeeSite lights that QLC+ doesn't ship a profile for.

| Fixture | File | Modes |
|---|---|---|
| YeeSite 60W RGB Pixel Light Bar (144 LEDs, 30 pixels) | [`YeeSite/YeeSite-60W-RGB-Pixel-Light-Bar.qxf`](YeeSite/YeeSite-60W-RGB-Pixel-Light-Bar.qxf) | 3, 5, 8, 90, 94 ch |

## Install

Copy the `.qxf` into your QLC+ user fixtures folder and restart QLC+:

- **macOS:** `~/Library/Application Support/QLC+/Fixtures/`
- **Windows:** `%USERPROFILE%\QLC+\Fixtures\`
- **Linux:** `~/.qlcplus/fixtures/`

It then appears under **YeeSite → 60W RGB Pixel Light Bar**.

## 60W RGB Pixel Light Bar — channel modes

Set the mode on the bar with MENU → `Addr` → ENTER, then UP/DOWN to pick `xx-CH`.

| Mode | Layout |
|---|---|
| 3 ch | Red, Green, Blue (whole bar) |
| 5 ch | Master dimmer, Strobe, Red, Green, Blue |
| 8 ch | Master dimmer, Strobe, Red, Green, Blue, Built-in Program, Program Speed, Program Background Colour |
| 90 ch | 30 pixels × RGB (R1 G1 B1 … R30 G30 B30) — 30 heads for the RGB Matrix |
| 94 ch | 30 pixels × RGB, then Strobe, Built-in Program, Program Speed, Program Background Colour (no master dimmer) |

**Strobe:** 0–9 off, 10–255 slow → fast.

**Built-in Program:**

| Value | Function |
|---|---|
| 0–2 | Off |
| 3–143 | Programs 1–47 (3 values each), colour from the RGB channels |
| 144–203 | Programs 48–67, preset colour |
| 204–206 | Program 68, cycles through programs 1–67 |
| 207–209 / 210–212 / 213–255 | Sound 1 / 2 / 3, colour from the RGB channels |

**Program Background Colour** applies to programs 1–47 and Sound 2–3. It is a 36-step table
in 7-value bands: black (0–6), then five levels (20, 38, 71, 133, 255) each of red, green,
blue, yellow, magenta, cyan and grey/white, ending with white at 245–255. The manual lists
238–243 then 245–255, skipping 244; the profile folds 244 into the 133-grey band.

## Sources

- The printed YeeSite user manual (DMX Traits pages and RGB Background Colour Table).
- Cross-checked against Lightkey's built-in "YeeSite – 60W RGB Pixel Light Bar" profile, which
  agrees on every channel.

Physical specs other than length (1 m) and power (60 W) aren't in the manual, so weight,
height, depth and lumens are left at 0. They don't affect control.

## Regenerating

The `.qxf` is generated so the 90 pixel channels and 70-odd program ranges stay consistent:

```bash
python3 generate_yeesite_60w_pixel_bar.py
```

Status: the XML validates and every mode resolves; not yet exercised against a bar in QLC+.
