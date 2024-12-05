import turtle

screen = turtle.Screen() #Ekranı seçiyoruz
screen.bgcolor("Grey") #Ekranın arkaplan rengini değiştiriyoruz 
kaplumba = turtle.Turtle(shape="turtle")
kaplumba.circle(80)

kaplumba.penup() #Kalemi Kaldırdı
kaplumba.setposition(-100,0) #pozisyon değiştirdi
kaplumba.pendown() #kalemi tekrar indirdi
kaplumba.circle(80) #daire çizdi

turtle.getscreen()._root.mainloop() #Çıkan panelin kapanmaması için 