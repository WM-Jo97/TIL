A='saFe eMotion Nail'

B=list(A.split(' '))
if B[0][-1].lower()==B[1][0].lower() and B[1][-1].lower()==B[2][0].lower() :
    print('Pass')
else:
    print('Fail')
