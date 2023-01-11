
def movetower(height,frompole,withpole,withpole1,topole):

    if height>=1:
        movetower(height-1,frompole,topole,withpole)
        movedisk(height,frompole,topole)
        movetower(height-1,withpole,frompole,topole)

def movedisk(disk,frompole,topole):
    print(f"Moving disk[{disk}]from{frompole}to{topole}")

M=input()
movetower(M,"1","2","3","4")