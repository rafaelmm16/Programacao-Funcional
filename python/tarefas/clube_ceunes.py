def m(e):
    if e>=0 and e<=30:
     h=180*1.8
     print ("Sua mensalidade é de",h)
    elif e>=31 and e<=39:
     f=180*1.7
     print ("Sua mensalidade é de",f)
    elif e>=40 and e<=79:
     g=180*1.65
     print ("Sua mensalidade é de",g)
    elif e>=80:
     print ("Você não pode participar.")
m(80)
