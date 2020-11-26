from fake_news.fake_news_predictor import FakeNews
import pytest


def test_FakeNews_0():
    fn = FakeNews(
        title="WATCH: MILO and Martin Shkreli March on UC Davis’ Campus - Breitbart",
        body="Breitbart editor MILO and former pharmaceutical executive Martin Shkreli will lead a rally this afternoon on UC Davis’ campus to protest the violent   speech activists who shut down  their event that was scheduled for last night.[  The rally, which is scheduled for 1 P. M. PST (4 PM EST) will feature both MILO and Shkreli and will take place on UC Davis’ quad. Last night’s event was cancelled after protesters became violent. Several protesters were caught by cameras attacking reporters and throwing barricades. “After consulting with UC Davis Police Department and UC Davis Student Affairs officials, the Davis College Republicans canceled tonight’s event featuring Breitbart columnist Milo Yiannopoulos,” claimed UC Davis in an official blog post on their website. “The decision was made at about 7:00 pm, 30 minutes prior to the scheduled start of the event, after a large number of protesters blocked access to the venue, and it was determined that it was no longer feasible to continue with the event safely. ”",
    )
    assert fn.score == 0.07496848805716592
    assert fn.RAG == "Green"


def test_FakeNews_1():
    fn = FakeNews(
        title="FLYNN: Hillary Clinton, Big Woman on Campus - Breitbart",
        body="'Ever get the feeling your life circles the roundabout rather than heads in a straight line toward the intended destination? [Hillary Clinton remains the big woman on campus in leafy, liberal Wellesley, Massachusetts. Everywhere else votes her most likely to don her inauguration dress for the remainder of her days the way Miss Havisham forever wore that wedding dress.  Speaking of Great Expectations, Hillary Rodham overflowed with them 48 years ago when she first addressed a Wellesley graduating class. The president of the college informed those gathered in 1969 that the students needed “no debate so far as I could ascertain as to who their spokesman was to be” (kind of the like the Democratic primaries in 2016 minus the   terms unknown then even at a Seven Sisters school). “I am very glad that Miss Adams made it clear that what I am speaking for today is all of us —  the 400 of us,” Miss Rodham told her classmates. After appointing herself Edger Bergen to the Charlie McCarthys and Mortimer Snerds in attendance, the    bespectacled in granny glasses (awarding her matronly wisdom —  or at least John Lennon wisdom) took issue with the previous speaker. Despite becoming the first   to win election to a seat in the U. S. Senate since Reconstruction, Edward Brooke came in for criticism for calling for “empathy” for the goals of protestors as he criticized tactics. Though Clinton in her senior thesis on Saul Alinsky lamented “Black Power demagogues” and “elitist arrogance and repressive intolerance” within the New Left, similar words coming out of a Republican necessitated a brief rebuttal. “Trust,” Rodham ironically observed in 1969, “this is one word that when I asked the class at our rehearsal what it was they wanted me to say for them, everyone came up to me and said ‘Talk about trust, talk about the lack of trust both for us and the way we feel about others. Talk about the trust bust.’ What can you say about it? What can you say about a feeling that permeates a generation and that perhaps is not even understood by those who are distrusted?” The “trust bust” certainly busted Clinton’s 2016 plans. She certainly did not even understand that people distrusted her. After Whitewater, Travelgate, the vast   conspiracy, Benghazi, and the missing emails, Clinton found herself the distrusted voice on Friday. There was a load of compromising on the road to the broadening of her political horizons. And distrust from the American people —  Trump edged her 48 percent to 38 percent on the question immediately prior to November’s election —  stood as a major reason for the closing of those horizons. Clinton described her vanquisher and his supporters as embracing a “lie,” a “con,” “alternative facts,” and “a   assault on truth and reason. ” She failed to explain why the American people chose his lies over her truth. “As the history majors among you here today know all too well, when people in power invent their own facts and attack those who question them, it can mark the beginning of the end of a free society,” she offered. “That is not hyperbole. ” Like so many people to emerge from the 1960s, Hillary Clinton embarked upon a long, strange trip. From high school Goldwater Girl and Wellesley College Republican president to Democratic politician, Clinton drank in the times and the place that gave her a degree. More significantly, she went from idealist to cynic, as a comparison of her two Wellesley commencement addresses show. Way back when, she lamented that “for too long our leaders have viewed politics as the art of the possible, and the challenge now is to practice politics as the art of making what appears to be impossible possible. ” Now, as the big woman on campus but the odd woman out of the White House, she wonders how her current station is even possible. “Why aren’t I 50 points ahead?” she asked in September. In May she asks why she isn’t president. The woman famously dubbed a “congenital liar” by Bill Safire concludes that lies did her in —  theirs, mind you, not hers. Getting stood up on Election Day, like finding yourself the jilted bride on your wedding day, inspires dangerous delusions.'",
    )
    assert fn.score == 0.5326171073576795
    assert fn.RAG == "Amber"


def test_FakeNews_2():
    fn = FakeNews(
        title="15 Civilians Killed In Single US Airstrike Have Been Identified",
        body="Videos 15 Civilians Killed In Single US Airstrike Have Been Identified The rate at which civilians are being killed by American airstrikes in Afghanistan is now higher than it was in 2014 when the US was engaged in active combat operations.   Photo of Hellfire missiles being loaded onto a US military Reaper drone in Afghanistan by Staff Sgt. Brian Ferguson/U.S. Air Force. \nThe Bureau has been able to identify 15 civilians killed in a single US drone strike in Afghanistan last month – the biggest loss of civilian life in one strike since the attack on the Medecins Sans Frontieres hospital (MSF) last October. \nThe US claimed it had conducted a “counter-terrorism” strike against Islamic State (IS) fighters when it hit Nangarhar province with missiles on September 28. But the next day the United Nations issued an unusually rapid and strong statement saying the strike had killed 15 civilians and injured 13 others who had gathered at a house to celebrate a tribal elder’s return from a pilgrimage to Mecca. \nThe Bureau spoke to a man named Haji Rais who said he was the owner of the house that was targeted. He said 15 people were killed and 19 others injured, and provided their names (listed below). The Bureau was able to independently verify the identities of those who died. \nRais’ son, a headmaster at a local school, was among them. Another man, Abdul Hakim, lost three of his sons in the attack. \nRais said he had no involvement with IS and denied US claims that IS members had visited his house before the strike. He said: “I did not even speak to those sort of people on the phone let alone receiving them in my house.” \nThe deaths amount to the biggest confirmed loss of civilian life in a single American strike in Afghanistan since the attack on the MSF hospital in Kunduz last October, which killed at least 42 people. \nThe Nangarhar strike was not the only US attack to kill civilians in September. The Bureau’s data indicates that as many as 45 civilians and allied soldiers were killed in four American strikes in Afghanistan and Somalia that month. \nOn September 18 a pair of strikes killed eight Afghan policemen in Tarinkot, the capital of Urozgan provice. US jets reportedly hit a police checkpoint, killing one officer, before returning to target first responders. The use of this tactic – known as a “double-tap” strike – is controversial because they often hit civilian rescuers. \nThe US told the Bureau it had conducted the strike against individuals firing on and posing a threat to Afghan forces. The email did not directly address the allegations of Afghan policemen being killed. \nAt the end of the month in Somalia, citizens burnt US flags on the streets of the north-central city of Galcayo after it emerged a drone attack may have unintentionally killed 22 Somali soldiers and civilians. The strike occurred on the same day as the one in Nangarhar. \nIn both the Somali and Afghan incidents, the US at first denied that any non-combatants had been killed. It is now investigating both the strikes in Nangarhar and Galcayo. \nThe rate at which civilians are being killed by American airstrikes in Afghanistan is now higher than it was in 2014 when the US was engaged in active combat operations. Name",
    )
    assert fn.score == 0.708754327229777
    assert fn.RAG == "Red"


def test_FakeNews_title_0():
    fn = FakeNews(
        "WATCH: MILO and Martin Shkreli March on UC Davis’ Campus - Breitbart",
    )
    assert fn.score == 0.036625672967898724
    assert fn.RAG == "Green"


def test_FakeNews_title_1():
    fn = FakeNews(
        "Trump Says Go Back, We Say Fight Back",
    )
    assert fn.score == 0.5455830046513762
    assert fn.RAG == "Amber"


def test_FakeNews_title_2():
    fn = FakeNews(
        "15 Civilians Killed In Single US Airstrike Have Been Identified",
    )
    assert fn.score == 0.853730521530615
    assert fn.RAG == "Red"


def test_FakeNews_int():
    with pytest.raises(TypeError):
        fn = FakeNews(
            104545,
        )
