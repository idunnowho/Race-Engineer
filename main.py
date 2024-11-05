from intro import menu, braking_prompt, downforce_prompt, suspension_prompt, gearing_prompt
import time

menu()

option = int(input(""))

x = 1

while True:
    if option == 1:
        braking_prompt()
        option = 0
    elif option == 2:
        downforce_prompt()
        option = 0
    elif option == 3:
        suspension_prompt()
        option = 0
    elif option == 4:
        gearing_prompt()
        option = 0
    else:
        time.sleep(3)
        menu()
        option = int(input(""))














#BRAKING
# if option == 1:
#     print("What seems to be the issue?")
#     print("(1) Not stopping in time?")
#     print("(2) Stopping to quick")
#     print("(3) Keep sliding when braking")
#     option = int(input(""))
#     if option == 1:
#         print(" -- Increase brake pressure ")
#         print(" -- Move Brake Bias")
#     elif option == 2:
#         print(" -- Lower Brake Pressure")
#     elif option == 3:
#         print("Is it in the front or the rear?")
#         option = input("")
#         if option == "front":
#             print(" -- Decrease Brake Pressure")
#             print(" -- Move Brake Brake Bias rearwards")
#         elif option == "rear":
#             print(" -- Move Brake Bias forwards")
#     else:
#         print("Enter 'front' or 'rear'")
#
#
# #DOWNFORCE
# elif option == 2:
#     print("What seems to be the issue?")
#     print("(1) Slow on Straights")
#     print("(2) Spinning out on fast corners")
#     print("(3) The car is not turning into corners")
#     option = int(input(""))
#     if option == 1:
#         print(" -- Reduce Front downforce")
#         print(" -- Reduce Rear Downforce")
#     elif option == 2:
#         print(" -- Raise Rear downforce")
#     elif option == 3:
#         print(" -- Reduce Rear downforce")
#     else:
#         print("Choose a number 1-3")
#
# #SUSPENSION
# elif option == 3:
#     print("What seems to be the issue?")
#     print("(1) Car doesn't turn in to corners (understeer)")
#     print("(2) Car turns too much (oversteer)")
#     print("(3) After a few laps, the tyres are gone")
#     option = int(input(""))
#     if option == 1:
#         print("(1) When turning in?")
#         print("(2) Throughout the corner?")
#         print("(3) On corner exit?")
#         option = int(input(""))
#         if option == 1:
#             print(" -- Stiffen the front spring rates")
#         elif option == 2:
#             print(" -- Stiffen rear anti-roll bars")
#         elif option == 3:
#             print(" -- Stiffen rear anti-roll bars")
#             print(" -- Raise ride height")
#         else:
#             print("Choose an number 1-3")
#     elif option == 2:
#         print("(1) When turning in?")
#         print("(2) Throughout the corner?")
#         print("(3) On corner exit?")
#         option = int(input(""))
#         if option == 1:
#             print(" -- Stiffen front anti-roll bars")
#             print(" -- Stiffen front spring rates")
#         elif option == 2:
#             print(" -- Soften rear anti-roll bars")
#         elif option == 3:
#             print(" -- Soften rear anti-roll bars")
#         else:
#             print("Choose an number 1-3")
#     elif option == 3:
#         print(" -- Stiffen front spring rates")
#         print(" -- Stiffen rear spring rates")
#     else:
#         print("Choose an number 1-3")
#
#
# #GEARING
# elif option == 4:
#     print("What seems to be the issue? ")
#     print("(1) Can't hit top speed")
#     print("(2) Slow acceleration")
#     option = int(input(""))
#     if option == 1:
#         print("Are you hitting the rev limiter on the longest straight? ")
#         option = input("")
#         if option == "yes":
#             print(" -- Increase final drive ratio")
#         elif option == "no":
#             print(" -- Lower final drive ratio")
#         else:
#             print("Choose 'yes' or 'no' ")
#     elif option == 2:
#         print(" -- Lower the final drive ratio.")
# else:
#     print("Please choose an number 1 - 4")

