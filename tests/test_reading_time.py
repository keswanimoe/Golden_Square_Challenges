from lib.reading_time import *
# Give a text and return esimated reading time
# reading_time('some text') -> 'The estimated reading time is 1 minute'

def test_reading_time_returns_one():
    # generate 200 words from chat gpt
    text = "Human curiosity has always propelled exploration, leading to remarkable discoveries and pushing the boundaries of knowledge. From ancient seafarers venturing into uncharted waters to modern-day space missions reaching for the stars, the spirit of exploration is ingrained in our history. Exploration encompasses various facets. It's the pursuit of the unknown, the desire to uncover hidden truths, and the bravery to challenge limits. Whether exploring outer space, the depths of oceans, or the frontiers of science, each endeavor brings a sense of wonder and possibility. Explorers like Magellan, Columbus, and Armstrong symbolize humanity's quest for exploration, courageously sailing uncharted seas or walking on alien landscapes. Yet, exploration isn't solely about physical journeys; it's also about intellectual quests. Scientists, artists, and thinkers explore realms of ideas, seeking innovation and understanding. Technological advancements have expanded our exploratory capabilities. Robotics, satellites, and telescopes delve into places humans cannot reach, unraveling mysteries of the cosmos and the Earth's depths. However, exploration isn't devoid of challenges. It poses risks, demands resilience, and sometimes comes with unforeseen consequences. Yet, it's through exploration that societies progress, evolve, and adapt. In essence, exploration embodies the human spirit's relentless pursuit of knowledge, pushing boundaries, and daring to go beyond what's."
    result = reading_time(text)
    # we return a float
    assert result == 'The estimated reading time is 1.0 minute'

def test_reading_time_returns_twentytwo():
    text = "Human curiosity has always propelled exploration, leading to remarkable discoveries and pushing the boundaries of knowledge. From ancient seafarers venturing into uncharted waters to modern-day space missions reaching for the stars, the spirit of exploration is ingrained in our history. Exploration encompasses various facets. It's the pursuit of the unknown, the desire to uncover hidden truths, and the bravery to challenge limits. Whether exploring outer space, the depths of oceans, or the frontiers of science, each endeavor brings a sense of wonder and possibility. Explorers like Magellan, Columbus, and Armstrong symbolize humanity's quest for exploration, courageously sailing uncharted seas or walking on alien landscapes. Yet, exploration isn't solely about physical journeys; it's also about intellectual quests. Scientists, artists, and thinkers explore realms of ideas, seeking innovation and understanding. Technological advancements have expanded our exploratory capabilities. Robotics, satellites, and telescopes delve into places humans cannot reach, unraveling mysteries of the cosmos and the Earth's depths. However, exploration isn't devoid of challenges. It poses risks, demands resilience, and sometimes comes with unforeseen consequences. Yet, it's through exploration that societies progress, evolve, and adapt. In essence, exploration embodies the human spirit's relentless pursuit of knowledge, pushing boundaries, and daring to go beyond what's."
    text_twentytwo = f' {text}' * 22
    result = reading_time(text_twentytwo)
    assert result == 'The estimated reading time is 22.0 minutes'