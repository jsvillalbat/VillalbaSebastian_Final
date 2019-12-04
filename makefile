resultado.png sigma.png solar.png: valores.txt datos.txt ode.dat
	python run.py
    
ode.dat : o.x
	./o.x > ode.dat

o.x : VillalbaSebastian_17.cpp
	c++ VillalbaSebastian_17.cpp -o o.x 

clean:
	rm ode.dat *.png *.x 