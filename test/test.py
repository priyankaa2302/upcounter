import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_upcounter(dut):

    dut._log.info("Start test")

    # Clock
    cocotb.start_soon(Clock(dut.clk, 10, unit="us").start())

    # Init
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Proper reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # Wait 1 cycle after reset (VERY IMPORTANT in TT CI)
    await ClockCycles(dut.clk, 1)

    expected = 0

    for i in range(10):
        await ClockCycles(dut.clk, 1)

        expected = (expected + 1) & 0xFF

        actual = dut.uo_out.value.integer

        dut._log.info(f"{i}: expected={expected}, got={actual}")

        assert actual == expected, \
            f"Mismatch at {i}: expected {expected}, got {actual}"
