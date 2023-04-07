# Take input of two sports
sports = input().split()

# Define the subjects and verbs
subjects = ["I", "We"]
verbs = ["play", "watch"]

# Loop through each subject
for subject in subjects:

    # Loop through each verb
    for verb in verbs:

        # Loop through each sport
        for sport in sports:

            # Generate and print the sentence
            print(subject, verb, sport+ ".")



    