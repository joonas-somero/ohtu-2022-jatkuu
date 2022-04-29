class IO:
    def tulosta(self, *merkkijonot):
        for mjono in merkkijonot:
            print(mjono)

    def lue(self, viesti):
        return input(viesti)

io = IO()
