

from curses import COLOR_CYAN
from turtle import left
from manim import *

# nettoyage ecran
class RemoveAllObjectsInScreen(Scene):
    def construct(self):
        self.add(
            VGroup(
                *[
                    VGroup(
                        *[
                            Dot()
                            for i in range(30)
                        ]
                    ).arrange_submobjects(RIGHT)
                    for j in range(10)
                ]
            ).arrange_submobjects(DOWN)
        )


# débuts de l'animation

class yooo(MovingCameraScene):
	
	def construct(self):
		self.play(self.camera.frame.animate.set(width=50))
		

		#EQUATION
		solna2=MathTex("{(a+b)}^{2}", color=WHITE)
		solna2.scale(1.5)
		solna3=MathTex(r"  c^2", color=WHITE)
		solna4=MathTex(r"+4\times"+r" \dfrac{ab}{2}", color=WHITE)
		solna3.scale(1.5)
		solna4.scale(1.5)
		egal =MathTex(r"=")
		egal.scale(1.5)
		egal.move_to(4.5*DOWN)
		#POSITIONING
		solna2.next_to(egal,LEFT)
		solna3.next_to(egal, RIGHT)
		solna4.next_to(solna3, RIGHT)
		



# dessin du carré et des lignes intermédiaires

		line4a=Line(np.array([-2,-2,0]), np.array([-2,-1,0]))
		line4b=Line(np.array([-2,-1,0]), np.array([-2,2,0]))
		line4a.set_color(YELLOW_A)
		line4b.set_color(BLUE)

		line3a=Line(np.array([1,-2,0]), np.array([2,-2,0]))
		line3b=Line(np.array([-2,-2,0]), np.array([1,-2,0]))
		line3a.set_color(YELLOW_A)
		line3b.set_color(BLUE)
		
		line2a=Line(np.array([2,2,0]), np.array([2,1,0]))
		line2b=Line(np.array([2,1,0]), np.array([2,-2,0]))
		line2a.set_color(YELLOW_A)
		line2b.set_color(BLUE)

		line1=Line(np.array([-2,2,0]), np.array([2,2,0]))		
		line2=Line(np.array([2,2,0]), np.array([2,-2,0]))
		line3=Line(np.array([2,-2,0]), np.array([-2,-2,0]))
		line4=Line(np.array([-2,-2,0]), np.array([-2,2,0]))
		self.play(Create(line1))
		self.play(Create(line2))
		self.play(Create(line3))
		self.play(Create(line4))
		self.wait(2)


		##insérer acolade 
		brace_test = Brace(mobject=line1, direction=UP,buff=1)
		somme = MathTex(r"a+b")
		somme.scale(1.5)
		somme.next_to(brace_test, UP)
		self.play(Write(somme))
		self.play(GrowFromCenter(brace_test))



		line1a=Line(np.array([-2,2,0]), np.array([-1,2,0]))
		line1b=Line(np.array([-1,2,0]), np.array([2,2,0]))
		self.play(FadeIn(line1a), FadeIn(line1b))
		self.wait(1.5)
		line1a.set_color(YELLOW_A)
		line1b.set_color(BLUE)
		text1a=Text("a", color=YELLOW_A)
		text1b=Text("b", color=BLUE)
		text1a.next_to(line1a, UP)
		text1b.next_to(line1b, UP)
		self.play(GrowFromCenter(text1a), GrowFromCenter(text1b))
		self.wait(2)



		#recoloration
		self.play(Create(line4a), Create(line4b),Create(line3a), Create(line3b),Create(line2a), Create(line2b))




		text4a=Text("a", color=YELLOW_A)
		text4b=Text("b", color=BLUE)
		text4a.next_to(line4a, LEFT)
		text4b.next_to(line4b, LEFT)

		text3a=Text("a", color=YELLOW_A)
		text3b=Text("b", color=BLUE)
		text3a.next_to(line3a, DOWN)
		text3b.next_to(line3b, DOWN)


		self.add(line2a, line2b)
		text2a=Text("a", color=YELLOW_A)
		text2b=Text("b", color=BLUE)
		text2a.next_to(line2a, RIGHT)
		text2b.next_to(line2b, RIGHT)
		self.play(GrowFromCenter(text2a), GrowFromCenter(text2b),GrowFromCenter(text3a), GrowFromCenter(text3b),GrowFromCenter(text4a), GrowFromCenter(text4b))


		self.wait(2)

		self.play(Write(solna2),Uncreate(brace_test),Uncreate(somme))
		self.wait(2)


		line5=Line(np.array([-1,2,0]), np.array([-2,-1,0]))
		line5.set_color(GREEN)
		self.play(Create(line5))
		text5c=Text("c", color=GREEN)
		text5c.next_to(text4b,4*RIGHT)
		self.wait()
		self.play(GrowFromCenter(text5c))
		self.wait(2.5)	

		line6=Line(np.array([-2,-1,0]), np.array([1,-2,0]))
		line6.set_color(GREEN)
		text6c=Text("c", color=GREEN)
		text6c.next_to(text2b,4*LEFT)


		line7=Line(np.array([1,-2,0]), np.array([2,1,0]))
		line7.set_color(GREEN)
		text7c=Text("c", color=GREEN)
		text7c.next_to(text3b,4*UP)

		line8=Line(np.array([2,1,0]), np.array([-1,2,0]))
		line8.set_color(GREEN)
		text8c=Text("c", color=GREEN)
		text8c.next_to(text1b,4*DOWN)

		self.play(Create(line6),Create(line7),Create(line8))
		self.play(GrowFromCenter(text8c),GrowFromCenter(text7c),GrowFromCenter(text6c))		


		self.wait(2)
		triangle1=Polygon(np.array([-1,2,0]), np.array([-2,2,0]), np.array([-2,-1,0]), fill_color=[PINK], fill_opacity=1)
		triangle2=Polygon(np.array([-2,-1,0]), np.array([-2,-2,0]), np.array([1,-2,0]), fill_color=[PINK], fill_opacity=1)
		triangle3=Polygon(np.array([1,-2,0]), np.array([2,-2,0]), np.array([2,1,0]), fill_color=[PINK], fill_opacity=1)
		triangle4=Polygon(np.array([2,1,0]), np.array([2,2,0]), np.array([-1,2,0]), fill_color=[PINK], fill_opacity=1)
		square=Polygon(np.array([2,1,0]), np.array([1,-2,0]), np.array([-2,-1,0]), np.array([-1,2,0]), fill_color=GREEN_E, fill_opacity=1)

		#on calcule les aires des petits triangles
		triangletext1=MathTex(r"\dfrac{ ab}{2}", color=BLACK)
		triangletext2=MathTex(r"\dfrac{ ab}{2}", color=BLACK)
		triangletext3=MathTex(r"\dfrac{ ab}{2}", color=BLACK)
		triangletext4=MathTex(r"\dfrac{ ab}{2}", color=BLACK)
		squaretext=MathTex("c^{2}", color=BLACK)
		triangletext1.scale(0.5)
		triangletext2.scale(0.5)
		triangletext3.scale(0.5)
		triangletext4.scale(0.5)
		squaretext.scale(1.2)

		#on les positionne
		triangletext1.move_to(1.6*LEFT + 1.5*UP)
		triangletext2.move_to(1.6*LEFT + 1.5*DOWN)
		triangletext3.move_to(1.6*RIGHT + 1.5*DOWN)
		triangletext4.move_to(1.6*RIGHT + 1.6*UP)
		

		#affifcher petit carré

		self.wait(3)
		self.play(Indicate(square))
		self.wait(1)
		self.play(Create(text8c),Create(text7c),Create(text6c),Create(text5c))		

		self.wait(2)
		self.play(ReplacementTransform(square.copy(), squaretext))
		self.wait(2)

		self.wait(1)
		self.play(Write(egal))
		self.wait(1)
		self.play(Write(solna3))
		aire = Text("égalité des aires")
		aire.next_to(egal, 1.5*DOWN)


		#et les petits triangles
		self.wait(2)
		self.play(Indicate(triangle1), Indicate(triangle2), Indicate(triangle3), Indicate(triangle4), run_time=3)
		self.add(line1a, line1b, line2a, line2b,line3a, line3b, line4a, line4b)
		self.wait(2)
		self.play(ReplacementTransform(triangle1.copy(), triangletext1), ReplacementTransform(triangle2.copy(), triangletext2), ReplacementTransform(triangle3.copy(), triangletext3), ReplacementTransform(triangle4.copy(), triangletext4))





		#on pose les équations
		self.wait(2)
		self.play(Write(solna4))
		self.wait(2)
		
		self.wait(2)

		int2=MathTex("a^2+2ab+b^2", color=WHITE)
		int2.scale(1.5)
		int2.next_to(egal,LEFT)
		self.play(ReplacementTransform(solna2,int2))
		self.wait(2)

		int3=MathTex("+2ab", color=WHITE)
		int3.scale(1.5)
		int3.next_to(solna3,RIGHT)
		self.play(ReplacementTransform(solna4,int3))
		self.wait(2)	

		fin=MathTex("a^2+b^2", color=WHITE)
		fin.scale(1.5)
		fin.next_to(egal,LEFT)
		self.play(ReplacementTransform(int2,fin),Uncreate(int3))
		self.wait(2)

	


		mobjects = VGroup(fin,egal,solna3)

		framebox1 = SurroundingRectangle(mobjects, buff = .1)
        
		self.play(
            Create(framebox1),
        )
		self.wait(5)