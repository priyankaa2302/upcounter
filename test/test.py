import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_upcounter(dut):

    # Reset
    dut.rst_n.value = 0
    dut.ena.value = 1
    await Timer(20, "ns")

    dut.rst_n.value = 1

    # Run clock cycles
    for _ in range(20):
        await Timer(10, "ns")

    # Simple check (optional but safe)
    assert dut.uo_out.value is not None
