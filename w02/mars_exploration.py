# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received
# by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.


def marsExploration(s):
    changed = 0
    for i in range(0, len(s), 3):
        if s[i] != "S":
            changed = changed + 1

        if s[i + 1] != "O":
            changed = changed + 1

        if s[i + 2] != "S":
            changed = changed + 1

    return changed


s = input("message: ")
print(marsExploration(s))
