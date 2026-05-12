import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_upcounter(dut):

    dut._log.info("Start")

    # Clock
    cocotb.start_soon(Clock(dut.clk, 10, unit="us").start())

    # Init
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset (IMPORTANT: hold longer)
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # Check counter
    expected = 0

    for i in range(10):
        await ClockCycles(dut.clk, 1)
        expected = (expected + 1) % 256

        assert dut.uo_out.value.integer == expected, \
            f"Mismatch: expected {expected}, got {dut.uo_out.value.integer}"
