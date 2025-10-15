from migen import *
from migen.sim import Simulator

class Divider8Bit(Module):
    def __init__(self):
        # Entrées
        self.dividend = Signal(8)
        self.divisor = Signal(8)
        self.start = Signal()
        
        # Sorties
        self.quotient = Signal(8)
        self.remainder = Signal(8)
        self.ready = Signal()
        self.done = Signal()  # Indique que les résultats sont valides
        
        # Internes
        self._count = Signal(4)
        self._remainder = Signal(9)  # 1 bit de plus
        self._quotient = Signal(8)
        self._dividend_reg = Signal(8)
        self._divisor_reg = Signal(8)
        
        self.submodules.fsm = FSM(reset_state="IDLE")
        
        # Ready est à 1 seulement dans l'état IDLE
        self.comb += self.ready.eq(self.fsm.ongoing("IDLE"))
        
        self.fsm.act("IDLE",
            NextValue(self.done, 0),
            If(self.start,
                NextValue(self._dividend_reg, self.dividend),
                NextValue(self._divisor_reg, self.divisor),
                NextValue(self._remainder, 0),
                NextValue(self._quotient, 0),
                NextValue(self._count, 0),
                NextState("SHIFT")
            )
        )
        
        # État SHIFT: décale remainder et ajoute le bit suivant du dividende
        self.fsm.act("SHIFT",
            NextValue(self._remainder, 
                (self._remainder << 1) | ((self._dividend_reg >> 7) & 1)),
            NextValue(self._dividend_reg, self._dividend_reg << 1),
            NextState("COMPARE")
        )
        
        # État COMPARE: compare et soustrait si possible
        self.fsm.act("COMPARE",
            If(self._remainder >= self._divisor_reg,
                NextValue(self._remainder, self._remainder - self._divisor_reg),
                NextValue(self._quotient, (self._quotient << 1) | 1)
            ).Else(
                NextValue(self._quotient, self._quotient << 1)
            ),
            NextValue(self._count, self._count + 1),
            If(self._count == 7,  # Après 8 itérations (0 à 7)
                NextState("DONE")
            ).Else(
                NextState("SHIFT")
            )
        )
        
        # État DONE: copie les résultats vers les sorties et signale la fin
        self.fsm.act("DONE",
            NextValue(self.quotient, self._quotient),
            NextValue(self.remainder, self._remainder[0:8]),
            NextValue(self.done, 1),
            NextState("IDLE")
        )


# === Testbench ===
def testbench(dut):
    tests = [
        (100, 10),   # Expected: 10 R 0
        (255, 5),    # Expected: 51 R 0
        (80, 7),     # Expected: 11 R 3
        (0, 3),      # Expected: 0 R 0
        (250, 250),  # Expected: 1 R 0
        (123, 1),    # Expected: 123 R 0
        (17, 3),     # Expected: 5 R 2
        (200, 8),    # Expected: 25 R 0
        (255, 1),    # Expected: 255 R 0
        (1, 255),    # Expected: 0 R 1
    ]
    
    for dividend, divisor in tests:
        print(f"Testing {dividend} / {divisor}")
        
        # Attendre que ready soit à 1
        while not (yield dut.ready):
            yield
        
        # Appliquer les entrées
        yield dut.dividend.eq(dividend)
        yield dut.divisor.eq(divisor)
        yield dut.start.eq(1)
        yield
        yield dut.start.eq(0)
        
        # Attendre que done passe à 1 (résultats valides)
        timeout = 0
        while not (yield dut.done):
            yield
            timeout += 1
            if timeout > 30:
                print("TIMEOUT!")
                break
        
        # Lire les résultats (ils sont maintenant valides)
        quotient = (yield dut.quotient)
        remainder = (yield dut.remainder)
        expected_q = dividend // divisor if divisor != 0 else 0
        expected_r = dividend % divisor if divisor != 0 else dividend
        
        print(f"  Result:   {dividend} / {divisor} = {quotient} R {remainder}")
        print(f"  Expected: {dividend} / {divisor} = {expected_q} R {expected_r}")
        
        if quotient == expected_q and remainder == expected_r:
            print("  ✓ PASS")
        else:
            print("  ✗ FAIL")
        
        print("-" * 50)


# === Simulation ===
if __name__ == "__main__":
    dut = Divider8Bit()
    sim = Simulator(dut, generators={"sys": [testbench(dut)]})
    sim.run()