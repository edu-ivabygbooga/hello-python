import time

questions = [
    {
        "question": "Vilken känd österrikisk filosof ägnade år åt att designa ett extremt minimalistiskt dörrhandtag i mässing till sin systers hus i Wien på 1920-talet?",
        "options": ["A) Karl Popper", "B) Ludwig Wittgenstein", "C) Friedrich Nietzsche", "D) Bertrand Russell"],
        "answer": "B",
        "fact": "Ludwig Wittgenstein var besatt av proportioner och lade enorm tid på att få dörrhandtagen och fönsterbeslagen i Haus Wittgenstein exakt rätt."
    },
    {
        "question": "Vad kallas den metallstång (vanligen 8x8 mm i Sverige) som går genom dörren och överför handtagets vridrörelse till låshuset?",
        "options": ["A) Fyrkantspinne (tryckespinne)", "B) Reglerbult", "C) Fallkolv", "D) Dorndjup"],
        "answer": "A",
        "fact": "Fyrkantspinnen (eller tryckespinnen) kopplar samman handtagen på båda sidor om dörrbladet."
    },
    {
        "question": "Vilken biologisk/kemisk egenskap gör att dörrhandtag i obehandlad mässing och koppar naturligt avdödar bakterier och virus inom ett par timmar?",
        "options": ["A) Piezoelektrisk effekt", "B) Oligodynamisk effekt", "C) Galvanisk induktion", "D) Termoelektrisk reaktion"],
        "answer": "B",
        "fact": "Den oligodynamiska effekten innebär att metalljoner förstör cellmembranet hos mikroorganismer, vilket gör oinredda kopparlegeringar självdesinficerande."
    },
    {
        "question": "Vad kallas den runda täckplattan som monteras på dörrbladet direkt bakom själva dörrhandtagets fäste?",
        "options": ["A) Slutbleck", "B) Rosett (tryckesrosett)", "C) Stolpe", "D) Kantskena"],
        "answer": "B",
        "fact": "Rosetten täcker håltagningen runt handtaget. Om plattan istället är lång och täcker både handtag och nyckelhål kallas den långskylt."
    },
    {
        "question": "Vilken afroamerikansk uppfinnare beviljades ett historiskt patent (US Patent 210,764) år 1878 för en förbättrad dörrstängnings- och dörrhandtagsmekanism?",
        "options": ["A) Elijah McCoy", "B) Osbourn Dorsey", "C) Lewis Latimer", "D) Garrett Morgan"],
        "answer": "B",
        "fact": "Osbourn Dorseys patent var ett av de tidigaste och mest inflytelserika i USA gällande mekaniska dörrhållare och spärrhandtag."
    }
]

def play_quiz():
    score = 0
    print("=" * 60)
    print(" 🚪 DET ULTIMATA (OCH OTROLIGT OBSKURA) DÖRRHANDTAGSQUIZET 🚪")
    print("=" * 60 + "\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Fråga {i}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")
            
        user_ans = input("\nDitt svar (A, B, C eller D): ").strip().upper()
        
        if user_ans == q["answer"]:
            print("\n✅ RÄTT! Imponerande koll på dörrbeslag och mekanik.")
            score += 1
        else:
            print(f"\n❌ FEL! Rätt svar var {q['answer']}.")
            
        print(f"💡 Nördfakta: {q['fact']}\n")
        print("-" * 60 + "\n")
        time.sleep(1)
        
    print(f"Spel slut! Du fick {score} av {len(questions)} rätt.\n")
    if score == len(questions):
        print("🏆 Titel: Certifierad Mästare på Dörrbeslag och Tryckesmekanik!")
    elif score >= 3:
        print("🥇 Titel: Erfaren Låssmed och Dörrentusiast.")
    else:
        print("🚪 Titel: Dörrhandtagsnovis. Dags att läsa på om Svensk Standard för byggbeslag!")

if __name__ == "__main__":
    play_quiz()