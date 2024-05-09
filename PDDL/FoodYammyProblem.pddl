(define (problem FoodYammyProblem)
	(:domain FoodYammyDomain)
	(:objects	c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13 c14 c15 - customer
				k1 k2 k3 k4 k5 k6 - kitchen
				v1 v2 v3 v4 v5 - vehicle
				n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18 n19 n20 n21 - node)
	(:init
	(= (total_distance) 0)
	(location_C c1 n1)
	(location_C c2 n2)
	(location_C c3 n3)
	(location_C c4 n4)
	(location_C c5 n5)
	(location_C c6 n6)
	(location_C c7 n7)
	(location_C c8 n8)
	(location_C c9 n9)
	(location_C c10 n10)
	(location_C c11 n11)
	(location_C c12 n12)
	(location_C c13 n13)
	(location_C c14 n14)
	(location_C c15 n15)
	(location_K k1 n16)
	(location_K k2 n17)
	(location_K k3 n18)
	(location_K k4 n19)
	(location_K k5 n20)
	(location_K k6 n21)
	(location_V v1 n1)
	(location_V v2 n2)
	(location_V v3 n3)
	(location_V v4 n4)
	(location_V v5 n5)
	(standBy v1)
	(standBy v2)
	(standBy v3)
	(standBy v4)
	(standBy v5)
	(K_HasFood_C k3 c1)
	(K_HasFood_C k5 c2)
	(K_HasFood_C k1 c3)
	(K_HasFood_C k6 c4)
	(K_HasFood_C k4 c5)
	(K_HasFood_C k2 c6)
	(K_HasFood_C k3 c7)
	(K_HasFood_C k5 c8)
	(K_HasFood_C k1 c9)
	(K_HasFood_C k6 c10)
	(K_HasFood_C k4 c11)
	(K_HasFood_C k2 c12)
	(K_HasFood_C k3 c13)
	(K_HasFood_C k5 c14)
	(K_HasFood_C k1 c15)
	(road n15 n10)
	(road n15 n8)
	(road n15 n11)
	(road n15 n20)
	(road n15 n21)
	(road n11 n21)
	(road n11 n5)
	(road n11 n9)
	(road n11 n15)
	(road n16 n4)
	(road n16 n10)
	(road n16 n6)
	(road n16 n11)
	(road n17 n7)
	(road n17 n16)
	(road n17 n13)
	(road n17 n3)
	(road n17 n21)
	(road n7 n1)
	(road n7 n4)
	(road n7 n17)
	(road n7 n19)
	(road n7 n6)
	(road n19 n7)
	(road n19 n16)
	(road n19 n17)
	(road n19 n15)
	(road n5 n4)
	(road n5 n19)
	(road n5 n14)
	(road n18 n3)
	(road n18 n20)
	(road n18 n5)
	(road n10 n7)
	(road n10 n2)
	(road n10 n4)
	(road n10 n18)
	(road n10 n19)
	(road n12 n13)
	(road n12 n9)
	(road n12 n15)
	(road n2 n21)
	(road n2 n8)
	(road n2 n18)
	(road n2 n12)
	(road n4 n13)
	(road n4 n2)
	(road n4 n12)
	(road n3 n10)
	(road n3 n14)
	(road n3 n13)
	(road n3 n16)
	(road n8 n1)
	(road n8 n3)
	(road n8 n17)
	(road n8 n18)
	(road n8 n11)
	(road n1 n16)
	(road n1 n8)
	(road n1 n12)
	(road n1 n6)
	(road n1 n21)
	(road n20 n9)
	(road n20 n14)
	(road n20 n1)
	(road n20 n8)
	(road n20 n18)
	(road n9 n5)
	(road n9 n2)
	(road n9 n13)
	(road n9 n1)
	(road n9 n15)
	(road n13 n7)
	(road n13 n9)
	(road n13 n14)
	(road n13 n11)
	(road n13 n6)
	(road n14 n1)
	(road n14 n17)
	(road n14 n19)
	(road n14 n16)
	(road n6 n12)
	(road n6 n20)
	(road n6 n8)
	(road n6 n15)
	(road n21 n14)
	(road n21 n10)
	(road n21 n3)
	(road n21 n17)
	(road n21 n20)
	(= (distance n15 n10) 10000)
	(= (distance n15 n8) 19600)
	(= (distance n15 n11) 6400)
	(= (distance n15 n20) 400000)
	(= (distance n15 n21) 392400)
	(= (distance n11 n21) 370000)
	(= (distance n11 n5) 14400)
	(= (distance n11 n9) 1600)
	(= (distance n11 n15) 6400)
	(= (distance n16 n4) 363600)
	(= (distance n16 n10) 392400)
	(= (distance n16 n6) 370000)
	(= (distance n16 n11) 400000)
	(= (distance n17 n7) 370000)
	(= (distance n17 n16) 400)
	(= (distance n17 n13) 408400)
	(= (distance n17 n3) 360400)
	(= (distance n17 n21) 6400)
	(= (distance n7 n1) 14400)
	(= (distance n7 n4) 3600)
	(= (distance n7 n17) 370000)
	(= (distance n7 n19) 363600)
	(= (distance n7 n6) 400)
	(= (distance n19 n7) 363600)
	(= (distance n19 n16) 3600)
	(= (distance n19 n17) 1600)
	(= (distance n19 n15) 408400)
	(= (distance n5 n4) 400)
	(= (distance n5 n19) 360400)
	(= (distance n5 n14) 32400)
	(= (distance n18 n3) 360000)
	(= (distance n18 n20) 1600)
	(= (distance n18 n5) 361600)
	(= (distance n10 n7) 3600)
	(= (distance n10 n2) 25600)
	(= (distance n10 n4) 14400)
	(= (distance n10 n18) 379600)
	(= (distance n10 n19) 374400)
	(= (distance n12 n13) 400)
	(= (distance n12 n9) 3600)
	(= (distance n12 n15) 3600)
	(= (distance n2 n21) 366400)
	(= (distance n2 n8) 14400)
	(= (distance n2 n18) 360400)
	(= (distance n2 n12) 40000)
	(= (distance n4 n13) 32400)
	(= (distance n4 n2) 1600)
	(= (distance n4 n12) 25600)
	(= (distance n3 n10) 19600)
	(= (distance n3 n14) 48400)
	(= (distance n3 n13) 40000)
	(= (distance n3 n16) 361600)
	(= (distance n8 n1) 19600)
	(= (distance n8 n3) 10000)
	(= (distance n8 n17) 374400)
	(= (distance n8 n18) 370000)
	(= (distance n8 n11) 3600)
	(= (distance n1 n16) 360000)
	(= (distance n1 n8) 19600)
	(= (distance n1 n12) 48400)
	(= (distance n1 n6) 10000)
	(= (distance n1 n21) 370000)
	(= (distance n20 n9) 366400)
	(= (distance n20 n14) 392400)
	(= (distance n20 n1) 366400)
	(= (distance n20 n8) 363600)
	(= (distance n20 n18) 1600)
	(= (distance n9 n5) 6400)
	(= (distance n9 n2) 19600)
	(= (distance n9 n13) 6400)
	(= (distance n9 n1) 25600)
	(= (distance n9 n15) 14400)
	(= (distance n13 n7) 14400)
	(= (distance n13 n9) 6400)
	(= (distance n13 n14) 400)
	(= (distance n13 n11) 1600)
	(= (distance n13 n6) 19600)
	(= (distance n14 n1) 67600)
	(= (distance n14 n17) 417600)
	(= (distance n14 n19) 400000)
	(= (distance n14 n16) 427600)
	(= (distance n6 n12) 14400)
	(= (distance n6 n20) 360400)
	(= (distance n6 n8) 1600)
	(= (distance n6 n15) 32400)
	(= (distance n21 n14) 385600)
	(= (distance n21 n10) 366400)
	(= (distance n21 n3) 363600)
	(= (distance n21 n17) 6400)
	(= (distance n21 n20) 400)
	)
	(:goal (and  (delivered c1)  (delivered c2)  (delivered c3)  (delivered c4)  (delivered c5)  (delivered c6)  (delivered c7)  (delivered c8)  (delivered c9)  (delivered c10)  (delivered c11)  (delivered c12)  (delivered c13)  (delivered c14)  (delivered c15) ))
	(:metric minimize (total_distance))
)
