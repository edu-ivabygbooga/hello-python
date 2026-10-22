#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import os

# ANSI-färgkoder för Splatoon-tema i terminalen
C_RESET   = "\033[0m"
C_BOLD    = "\033[1m"
C_YELLOW  = "\033[93m"  # Splatoon 3 Yellow
C_PURPLE  = "\033[95m"  # Deep Purple / Ink
C_CYAN    = "\033[96m"  # Cyan Ink
C_GREEN   = "\033[92m"  # Success / Rank Up
C_RED     = "\033[91m"  # Splat / Wrong
C_BLUE    = "\033[94m"  # Info
C_MAGENTA = "\033[35m"

def clear():
    """Rensar skärmen beroende på OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(f"{C_PURPLE}{C_BOLD}")
    print(r"""
   ███████╗██████╗ ██╗      █████╗ ████████╗██████╗ ██╗  ██╗███╗   ██╗
   ██╔════╝██╔══██╗██║     ██╔══██╗╚══██╔══╝██╔══██╗██║  ██║████╗  ██║
   ███████╗██████╔╝██║     ███████║   ██║   ██║  ██║██║  ██║██╔██╗ ██║
   ╚════██║██╔═══╝ ██║     ██╔══██║   ██║   ██║  ██║██║  ██║██║╚██╗██║
   ███████║██║     ███████╗██║  ██║   ██║   ██████╔╝╚█████╔╝██║ ╚████║
   ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚════╝ ╚═╝  ╚═══╝
    """ + C_RESET)
    print(f"{C_YELLOW}{C_BOLD}   === ULTIMATE OBSCURE META & COMPETITIVE QUIZ ==={C_RESET}\n")

QUESTIONS = [
    {
        "id": 1,
        "era": "Splatoon 1 Meta",
        "question": "I Splatoon 1 var Quick Respawn (QR) extremt dominant. Vad var den avgörande mekaniska skillnaden på hur QR fungerade i Splatoon 1 jämfört med hur det ändrades i Splatoon 2/3?",
        "options": {
            "A": "I Splatoon 1 aktiverades QR vid VARJE död, oavsett om du fick kills i ditt förra liv eller inte.",
            "B": "I Splatoon 1 gav QR även full Special Saver automatiskt utan att ladda ur mätaren.",
            "C": "I Splatoon 1 fungerade QR enbart om man samtidigt bar Stealth Jump.",
            "D": "I Splatoon 1 gav QR 50% snabbare simhastighet direkt efter respawn."
        },
        "answer": "A",
        "explanation": "I Splatoon 1 fanns ingen begränsning! Man kunde stapla 3 mains / 9 subs QR och återuppstå på ~1.5 sekunder varje gång man dog, oavsett om man tagit 10 kills i rad innan. I S2 patch 1.4.0 ändrades QR till att enbart aktiveras om man dör utan att ha eliminerat någon i sitt förra liv."
    },
    {
        "id": 2,
        "era": "Splatoon 2 Patch History",
        "question": "Under Splatoon 2 dominerades tävlingsscenen av Main Power Up (MPU) på vapen som Bamboozler 14 och Kensa Splattershot Pro. Vad var det exakta skade-taket (damage cap) per skott som Nintendo tvingades lägga in på Bamboozler för att förhindra äkta 1-shot kills?",
        "options": {
            "A": "49.9 skada",
            "B": "99.0 skada",
            "C": "99.9 skada",
            "D": "100.0 skada men med halverad räckvidd"
        },
        "answer": "C",
        "explanation": "Nintendo capade Bamboozler MPU-skada till exakt 99.9 skada. Eftersom motståndare tog 0.1 skada nästan omedelbart när de nuddade fientligt bläck på marken, räknades 99.9 skada i praktiken ändå som ett 1-shot kill i tävlingsmatcher!"
    },
    {
        "id": 3,
        "era": "Competitive Esports History",
        "question": "Det legendariska japanska laget GGBoyz dominerade Splatoon 2 helt och vann både World Championship 2018 och 2019. Vilken spelare i laget var känd som deras obestridliga Dynamo Roller- och Heavy Splatling-specialist?",
        "options": {
            "A": "Taiji",
            "B": "Dynamon",
            "C": "Yamamicchi",
            "D": "Eton"
        },
        "answer": "B",
        "explanation": "Dynamon anses vara en av historiens största Splatoon-spelare någonsin. Hans otroliga positioning med Dynamo Roller och Heavy Splatling var hörnstenen i GGBoyz dominans mot både japanska och västerländska lag."
    },
    {
        "id": 4,
        "era": "Splatoon 3 Launch Meta (Ver 1.1.0)",
        "question": "Vid lanseringen av Splatoon 3 (Patch 1.1.0) var ett visst huvudvapen med Fizzy Bomb och Booyah Bomb så absurt överlägset på grund av sina hitboxar och kit-synergier att nästan alla tävlingslag körde minst en (eller två) i sin comp. Vilket vapen?",
        "options": {
            "A": "Sloshing Machine (Kaffebryggaren)",
            "B": "Splash-o-matic",
            "C": "Flingza Roller",
            "D": "Bloblobber"
        },
        "answer": "A",
        "explanation": "Sloshing Machine Ver 1.1.0 hade gigantiska hitboxes som skadade spelare långt bakom väggar och avsatser, kombinerat med Fizzy Bomb för snabb rörelse/paint och Booyah Bomb för instant invulnerability. Den nerfastes kraftigt i patch 1.2.0 och 2.0.0."
    },
    {
        "id": 5,
        "era": "Splatoon 2 Mechanics & Math",
        "question": "Hur fungerade 'Damage Bleed-Through Cap' för Ink Armor i Splatoon 2 när en spelare med aktiverad Ink Armor (30 HP) blev träffad av ett fullt laddat E-liter 4K-skott (180 skada)?",
        "options": {
            "A": "Spelaren dog direkt eftersom 180 skada överstiger 30 HP med mer än 100.",
            "B": "Ink Armor tog emot hela skadan och spelaren tog 0 skada oavsett hur starkt skottet var.",
            "C": "Ink Armor bröts, men den överskjutande skadan som fördes över till spelaren var spärrad till max 80 HP, vilket gjorde att en spelare med full hälsa överlevde med 20 HP.",
            "D": "Skadan reflekterades tillbaka på E-liter-skytten."
        },
        "answer": "C",
        "explanation": "För att förhindra att snipers/chargers direkt knockade folk genom Ink Armor lade Nintendo till en spärr: skadeöverföringen ('bleed-through') kunde max vara 80 HP från ett enskilt skott. En spelare på 100 HP tog 80 skada, slungades bakåt av knockback, men överlevde på 20 HP!"
    },
    {
        "id": 6,
        "era": "Splatoon 1 Map History",
        "question": "Varför togs kartan Saltspray Rig (Saltförrådet) bort från officiella turneringsrotationer och Ranked-rotationer väldigt tidigt i Splatoon 1?",
        "options": {
            "A": "Asymmetrisk layout och 'Right-Hand Advantage' gav det lag som startade på den ena sidan en enorm, orättvis fördel i att kontrollera den övre zonen.",
            "B": "Kartan led av minnesläckor som fick Spelet att krascha under LAN-turneringar.",
            "C": "Tornet i Tower Control kunde fastna i kranarna på mitten av kartan.",
            "D": "Rainmaker kunde kastas ut ur kartan på ett sätt som gjorde att matchen inte kunde avslutas."
        },
        "answer": "A",
        "explanation": "Saltspray Rig var asymmetrisk. Eftersom kameran i Splatoon sitter över spelarens högra axel (Right-Hand Advantage), hade laget som anlände till den övre zonen från den gynnade sidan en gigantisk peeking-fördel runt väggarna som det andra laget inte kunde matcha."
    },
    {
        "id": 7,
        "era": "Splatoon 3 High-Level Strategy",
        "question": "Vad kännetecknar den populära tävlingsstrategin 'Zombie Comp' / 'QR-Cooler Push' i Splatoon 3?",
        "options": {
            "A": "Att spela 4 stycken Wiper Decavitator för att förhindra att motståndarna färgar marken.",
            "B": "Att kombinera Tacticooler (100% Instant Respawn + Special Saver) med Quick Respawn gear på aggressiva frontlines för att konstant attackera utan respawn-straff.",
            "C": "Att stå kvar i sin egen spawn i 2 minuter för att bygga upp 4 x Tenta Missiles samtidigt.",
            "D": "Att utnyttja Super Jump för att göra alla spelare osynliga på minikartan under hela matchen."
        },
        "answer": "B",
        "explanation": "Tacticooler ger under 15 sekunder 1-frame respawn och 100% Special Saver. När detta kombineras med Quick Respawn (Zombie) kan korta frontlinje-vapen (t.ex. Tri-Slosher, N-ZAP, S-BLAST) kasta sig in i motståndarens linjer oavbrutet – om de dör är de tillbaka på banan nästan direkt!"
    },
    {
        "id": 8,
        "era": "Splatoon 2 Special Meta",
        "question": "I Splatoon 2 var Sting Ray (Strålkanonen) ett av de mest centraliserande specialvapnen någonsin, särskilt i Tower Control på kartan Port Mackerel. Varför var den så extremt brutalt opåverkbar där?",
        "options": {
            "A": "Port Mackerels långa, smala och raka korridorer gjorde att Sting Ray från egen spawn kunde täcka hela tornets färdväg genom väggar utan motspel.",
            "B": "Sting Ray kunde stoppa timer-räknaren permanent om man sköt på tornet.",
            "C": "Port Mackerel saknade Sponge-block som annars stoppade Sting Ray.",
            "D": "Sting Ray laddades upp dubbelt så snabbt på Port Mackerel på grund av en ban-bugg."
        },
        "answer": "A",
        "explanation": "Port Mackerel var byggd av långa, parallella container-gångar. Sting Ray sköt rakt igenom alla väggar över hela kartans längd. En spelare som stod tryggt i sin egen spawn kunde med lätthet stråla tornet och döda alla som stod på det, vilket gjorde torn-pushar nästan omöjliga utan egen Sting Ray-counter."
    },
    {
        "id": 9,
        "era": "Fundamental Movement & Positioning",
        "question": "Vad innebär det taktiska konceptet 'Right-Hand Advantage' (RHA) i tävlings-Splatoon?",
        "options": {
            "A": "Att höger trigger-knapp har 2 frames snabbare input latency än vänster trigger.",
            "B": "Att Inklings håller vapnet på höger sida, vilket gör att man kan peeka och skjuta runt högra hörn/hinder medan ~80% av ens egen kropp förblir i skydd bakom väggen.",
            "C": "Att man simmar 10% snabbare om man svänger kameran åt höger.",
            "D": "Att Squid Roll ger fler invincibility frames om man rullar åt höger."
        },
        "answer": "B",
        "explanation": "Eftersom karaktärerna är högerhänta och kameran sitter över höger axel kan du titta och skjuta runt ett hinder åt HÖGER med minimal exponering av din egen hitbox. Peekar du åt VÄNSTER måste hela din kropp gå ut från väggen innan ditt vapen har fri siktlinje!"
    },
    {
        "id": 10,
        "era": "Splatoon 3 Early Meta (2022-2023)",
        "question": "Under det första året av Splatoon 3 var 'Splash-o-matic' det obestridda S-tier-vapnet i turneringar världen över. Vilken kombination av egenskaper gjorde att lag ofta körde dubbla (2x) Splash-o-matic?",
        "options": {
            "A": "0° spridning när man hoppar (perfekt precision), 200p Crab Tank (dåtidens starkaste special) och Burst Bomb för snabb paint och synergier.",
            "B": "Vapnet hade 50% längre räckvidd än E-liter 4K och kostade bara 150p för special.",
            "C": "Splash-o-matic kunde kasta tre Torpedo-bomber samtidigt.",
            "D": "Det var det enda vapnet som kunde skada Squid Beacons genom väggar."
        },
        "answer": "A",
        "explanation": "Splash-o-matic hade perfekt skjutprecision även i luften, galen målningsförmåga, Burst Bomb för instant combo/chip damage, och tillgång till Crab Tank för bara 200p. Detta gjorde vapnet till den mest stabila och mångsidiga frontlinjen under hela tidiga Splatoon 3-eran!"
    }
]

RANKS = [
    (10, "S+50 / X-RANK TOP 500 COMP GOD 🏆", "Du är en levande Splatoon-encyklopedi! Du har läst varje patch note sedan 2015, kan Sendou.ink utantill och har förmodligen vunnit en Area Cup eller LUTI Division 1!"),
    (8,  "X-RANK META ANALYST 🥇", "Otroligt bra resultat! Du har koll på MPU-siffror, Ink Armor bleed-through och tävlingshistorik på högsta nivå."),
    (5,  "S+ SOLO QUEUE WARRIOR 🥈", "Snyggt jobbat! Du har bra koll på grundläggande meta och känner igen de största namnen och vapnen, men föll på de mest obskyra mekanikerna."),
    (3,  "A- RANK CASUAL COMPETITOR 🥉", "Helt okej! Du spelar troligtvis mycket Ranked/Anarchy, men det är dags att läsa på om frame data och turneringshistorik på Sendou.ink!"),
    (0,  "TURF WAR CASUAL 🦑", "Oj då! Du blev splattad direkt på spännet. Dags att gå tillbaka till Inkopolis och studera patch notes från Splatoon 1 till 3!")
]

def run_quiz():
    clear()
    print_banner()
    print(f"{C_CYAN}Välkommen! Detta frågesportstest prövar din kunskap om Splatoon Comp & Meta.{C_RESET}")
    print(f"Det finns {len(QUESTIONS)} obskyra frågor. Svara med A, B, C eller D.\n")
    input(f"{C_YELLOW}Tryck på ENTER för att starta spelet...{C_RESET}")

    score = 0
    streak = 0
    max_streak = 0

    for i, q in enumerate(QUESTIONS, start=1):
        clear()
        print_banner()
        print(f"{C_BLUE}[Fråga {i}/{len(QUESTIONS)}] - Era/Kategori: {C_BOLD}{q['era']}{C_RESET}")
        print(f"{C_YELLOW}Streak: {streak} 🔥 | Poäng: {score}/{i-1}{C_RESET}\n")
        print(f"{C_BOLD}{q['question']}{C_RESET}\n")

        for key, opt in q['options'].items():
            print(f"  {C_CYAN}{key}){C_RESET} {opt}")

        print()
        while True:
            user_choice = input(f"{C_BOLD}Ditt svar (A/B/C/D): {C_RESET}").strip().upper()
            if user_choice in ["A", "B", "C", "D"]:
                break
            print(f"{C_RED}Ogiltigt val! Ange A, B, C eller D.{C_RESET}")

        if user_choice == q["answer"]:
            score += 1
            streak += 1
            if streak > max_streak:
                max_streak = streak
            print(f"\n{C_GREEN}{C_BOLD}RÄTT! 🎉{C_RESET}")
            print(f"{C_GREEN}Streak: {streak} i rad!{C_RESET}")
        else:
            streak = 0
            correct_letter = q["answer"]
            correct_text = q["options"][correct_letter]
            print(f"\n{C_RED}{C_BOLD}FEL! 💥 (Du svarade {user_choice}){C_RESET}")
            print(f"{C_YELLOW}Rätt svar var {correct_letter}: {correct_text}{C_RESET}")

        print(f"\n{C_MAGENTA}{C_BOLD}💡 META-BAKGRUND & FÖRKLARING:{C_RESET}")
        print(f"{C_MAGENTA}{q['explanation']}{C_RESET}\n")

        if i < len(QUESTIONS):
            input(f"{C_YELLOW}Tryck på ENTER för nästa fråga...{C_RESET}")

    clear()
    print_banner()
    print(f"{C_BOLD}{C_YELLOW}=== TÄVLINGSRESULTAT ==={C_RESET}\n")
    print(f"Totalt antal poäng: {C_BOLD}{score} / {len(QUESTIONS)}{C_RESET}")
    print(f"Högsta Win-Streak:  {C_BOLD}{max_streak}{C_RESET}\n")

    final_rank_title = ""
    final_rank_desc = ""
    for min_score, title, desc in RANKS:
        if score >= min_score:
            final_rank_title = title
            final_rank_desc = desc
            break

    print(f"Din comp-rank: {C_GREEN}{C_BOLD}{final_rank_title}{C_RESET}")
    print(f"{C_CYAN}{final_rank_desc}{C_RESET}\n")

    print(f"{C_PURPLE}Tack för att du spelade! Stay Fresh! / Catch Ya Later! 🦑🐙{C_RESET}\n")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nSpelet avbröts. Vi ses i Inkopolis!")
        sys.exit(0)