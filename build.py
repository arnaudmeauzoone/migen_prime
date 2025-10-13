from migen import *
import sipeed_tang_primer20k

class VideoTop(Module):
    def __init__(self, platform):
        self.number = Signal(16)
        self.is_prime = Signal()

        # Précondition : nombre ≥ 2
        is_valid = Signal()
        self.comb += is_valid.eq(self.number >= 2)

        # Génération des flags de divisibilité
        div_flags = []
        for d in range(2, 256):
            div = Signal()
            div_flags.append(div)

            # Liste des multiples de d jusqu'à 65535
            multiples = [i for i in range(d, 65536, d)]

            # Comparaison combinatoire : number == i pour chaque multiple
            comparisons = [self.number == i for i in multiples]
            self.comb += div.eq(comparisons[0])
            for cmp in comparisons[1:]:
                self.comb += div.eq(div | cmp)

        # Agrégation : si divisible par un d → pas premier
        any_divisible = Signal()
        self.comb += any_divisible.eq(div_flags[0])
        for div in div_flags[1:]:
            self.comb += any_divisible.eq(any_divisible | div)

        # Résultat final
        self.comb += self.is_prime.eq(is_valid & ~any_divisible)

# Verilog generation
if __name__ == "__main__":
    platform = sipeed_tang_primer20k.Platform()

    fragmentg = VideoTop(platform)
    platform.finalize(fragment=fragmentg)
    v = platform.get_verilog(fragment=fragmentg)
    v.write("prime.v")
    print("Verilog file generated: prime.v")
