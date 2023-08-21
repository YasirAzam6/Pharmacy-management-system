from Pharmacist import Pharmacist  # Class file for Pharmacist
from Worker import Worker  # Class file for Worker


def main():
   while True:
    opt = eval(input('''Are you a:
    1. Worker
    2. Pharmacist
    
    Select Desired option
        '''))

    print("\n\n")

    if opt == 1:
        Worker()
    elif opt == 2:
        Pharmacist()
    else:
        print('''No such option available...
        Exiting Program!
        ...1
        ..
        .''')

        # main() end


main()
