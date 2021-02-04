import random

rouleur_deck=[3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
sprinteur_deck=[2,2,2,3,3,3,4,4,4,5,5,5,5,9,9,9]

peleton_deck=[[3],[3],[3],[4],[4],[4],[5],[5],[5],[6],[6],[6],[7],[7],[7],[2,9],[2,9]]

face_up_rouleur=[]
face_up_sprinteur=[]
face_up_peleton=[]
used_cards_rouleur=[]
used_cards_sprinteur=[]
used_cards_peleton=[]

def rouleur(start, fu, uc):
    if len(start)==0 and len(fu)==0:
        to_return=[2,start,fu]
    else:
        if len(start)==0:
            for i in range(len(fu)):
                start.append(fu[i])
            
            energy_deck=start
            
            for i in range(len(fu)):
                fu.pop(0)
            face_up=fu
        else:
            energy_deck=start
            face_up=fu

        picked_up=card_picker(energy_deck)
        for i in range(len(picked_up)):
            energy_deck.remove(picked_up[i])
            
        
        chosen_card=card_choice(picked_up)
        picked_up.remove(chosen_card)
        for i in range(len(picked_up)):

            face_up.append(picked_up[i])
        uc.append(chosen_card)
        to_return=[chosen_card,energy_deck,face_up]

    return to_return

def sprinteur():
    if len(sprinteur_deck)==0 and len(face_up_sprinteur)==0:
        to_return=[2,sprinteur_deck,face_up_sprinteur]
    else:
        if len(sprinteur_deck)==0:
            for i in range(len(face_up_sprinteur)):
                sprinteur_deck.append(face_up_sprinteur[i])
            
            energy_deck=sprinteur_deck
            
            for i in range(len(face_up_sprinteur)):
                face_up_sprinteur.pop(0)
            face_up=face_up_sprinteur
        else:
            energy_deck=sprinteur_deck
            face_up=face_up_sprinteur

        picked_up=card_picker(energy_deck)
        for i in range(len(picked_up)):
            energy_deck.remove(picked_up[i])
            
        
        chosen_card=card_choice(picked_up)
        picked_up.remove(chosen_card)
        for i in range(len(picked_up)):

            face_up.append(picked_up[i])
        used_cards_rouleur.append(chosen_card)
        to_return=[chosen_card,energy_deck,face_up]

    return to_return

def peleton():
    if len(peleton_deck)==0 and len(face_up_peleton)==0:
        to_return=[[2],peleton_deck,face_up_peleton]
    else:    
        if len(peleton_deck)==0:
            for i in range(len(face_up_peleton)):
                peleton_deck.append(face_up_peleton[i])
            
            energy_deck=peleton_deck
            
            for i in range(len(face_up_peleton)):
                face_up_peleton.pop(0)
            face_up=face_up_peleton
        else:
            energy_deck=peleton_deck
            face_up=face_up_peleton

        picked_up=card_picker(energy_deck)
        for i in range(len(picked_up)):
            energy_deck.remove(picked_up[i])
            
        
        chosen_card=card_choice(picked_up)
        picked_up.remove(chosen_card)
        for i in range(len(picked_up)):

            face_up.append(picked_up[i])
        used_cards_rouleur.append(chosen_card)
        to_return=[chosen_card,energy_deck,face_up]

    return to_return

#Just the beginings of Peleton team will further complete when combined with track for the 2,9 move
def card_picker(energy_deck):
    picked_up=[]
    if len(energy_deck)>=4:
        picked_up+=random.sample(energy_deck,4)
    else:
        picked_up+=energy_deck
    
    return picked_up

def card_choice(hand):
    return hand[0]