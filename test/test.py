# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_upcounter(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Checking counter increments")
    expected =0

     for i in range(10):
        await ClockCycles(dut.clk, 1)

        expected = (expected + 1) % 256

        dut._log.info(f"Cycle {i}: expected={expected}, got={dut.uo_out.value}")

        assert dut.uo_out.value == expected, \
            f"Mismatch at cycle {i}: expected {expected}, got {dut.uo_out.value}"
