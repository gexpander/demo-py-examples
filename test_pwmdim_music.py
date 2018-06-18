import time

import gex

# beeping music with PWM (square wave)

C3  = 130.81; Cx3 = 138.59; D3  = 146.83; Dx3 = 155.56; E3  = 164.81; F3  = 174.61
Fx3 = 185.00; G3  = 196.00; Gx3 = 207.65; A3  = 220.00; Ax3 = 233.08; B3  = 246.94
C4  = 261.63; Cx4 = 277.18; D4  = 293.66; Dx4 = 311.13; E4  = 329.63; F4  = 349.23
Fx4 = 369.99; G4  = 392.00; Gx4 = 415.30; A4  = 440.00; Ax4 = 466.16; B4  = 493.88
C5  = 523.25; Cx5 = 554.37; D5  = 587.33; Dx5 = 622.25; E5  = 659.25; F5  = 698.46
Fx5 = 739.99; G5  = 783.99; Gx5 = 830.61; A5  = 880.00; Ax5 = 932.33; B5  = 987.77

with gex.Client(gex.TrxRawUSB()) as client:
    pwm = gex.PWMDim(client, 'dim')

    # O   O/ #/ #~ #=
    # 16, 8, 4, 2, 1
    notes = [
        (G3, 2),
        (G4, 2), (E4, 6), (G4, 2), (E4, 2), (A4, 6), (0, 2), (B4, 2),
        (G4, 2), (E4, 6), (A4, 2), (G4, 2), (D4, 6), (0, 2), (G3, 2),

        (G4, 2), (E4, 6), (D4, 2), (C4, 2), (C5, 6), (0, 2), (A4, 2),
        (G4, 2), (E4, 4), (0, 2), (D4, 2), (A3, 2), (C4, 6), (0, 2), (G3, 2),

        #rep
        (G4, 2), (E4, 6), (G4, 2), (E4, 2), (A4, 6), (0, 2), (B4, 2),
        (G4, 2), (E4, 6), (A4, 2), (G4, 2), (D4, 6), (0, 2), (G3, 2),

        (G4, 2), (E4, 6), (D4, 2), (C4, 2), (C5, 6), (0, 2), (A4, 2),

        (G4, 2), (E4, 6), (D4, 2), (A3, 2), (C4, 6), (0, 2), #(C4, 2),
    ]

    for p in notes:
        pwm.stop()
        time.sleep(0.01)
        f = round(p[0])
        print(f)
        if f > 0:
            pwm.set_frequency(f)
            pwm.start()
        time.sleep(0.1*p[1])

    pwm.stop()

