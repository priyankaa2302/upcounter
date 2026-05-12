Here is a **shortened Tiny Tapeout datasheet version**:

## How it works

This project is an **8-bit up counter**. On every rising edge of the clock (`clk`), the counter increases by 1. When it reaches 255, it wraps back to 0. The counter resets to 0 when `rst_n = 0`. The current count is shown on `uo_out[7:0]`.

## How to test

Apply a clock to `clk` and set `ena = 1`. First pulse `rst_n = 0` to reset, then set it to `1`. The output `uo_out` will increment every clock cycle:

0 → 1 → 2 → ... → 255 → 0

Use GTKWave or Cocotb to observe the waveform.

## External hardware

No external hardware required.
Optional: Connect `uo_out[7:0]` to 8 LEDs to display the count.
