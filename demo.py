from manim import *
from manim_play_timeline import play_timeline


class Test(Scene):
    """Example showing how to use play_timeline."""
    def construct(self):

        # Create a number line which will be used as a progress bar
        n = NumberLine(include_numbers=True, x_range=[0,12]).to_edge(DOWN)
        self.add(n)
        progress_bar = Line(n.n2p(0), n.n2p(12)).set_stroke(color=YELLOW, opacity=0.5, width=20)

        # Create a timeline of animations. One of the animations is the progress bar itself
        # going from 0 to 12 in 12 seconds. It can be used as a reference to check that
        # the other animations are playing at the right time.
        timeline = {
            0: Create(progress_bar, run_time=12, rate_func=linear),
            1: Create(Square(), run_time=10),
            2: [Create(Circle(), run_time=4),
                Create(Triangle(), run_time=2)],
            9: Write(Text("It works!").next_to(progress_bar, UP, buff=1), 
                     run_time=3)
        }
        play_timeline(self, timeline)
        self.wait()
