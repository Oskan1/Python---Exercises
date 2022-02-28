from prescription_data import *
from prescription_data import patients

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin) #without remove, we cant access line 11 for exception error!
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial")
    print(patient, prescription)

# now we know difference between remove and discard, its time to check POP method
print("MEW LINEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)