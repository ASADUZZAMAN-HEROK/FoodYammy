(define (domain FoodYammyDomain)
  (:requirements :strips :typing :adl :fluents :action-costs)
  
  (:types kitchen customer vehicle node)
  
  (:predicates (road ?node ?node)
         (location_K ?kitchen ?node)
			   (location_C ?customer ?node)
			   (location_V ?vehicle ?node)
			   (K_HasFood_C ?kitchen ?customer)
			   (V_HasFood_C ?vehicle ?customer)
			   (standBy ?vehicle)
			   (delivered ?customer))
			   
	(:functions (total_distance)
                (distance ?node ?node)
	)

  (:action move
    :parameters (?v - vehicle ?cur - node ?next - node)
    :precondition (and (location_V ?v ?cur) (road ?cur ?next))
    :effect (and (not (location_V ?v ?cur)) (location_V ?v ?next) (increase (total_distance) (distance ?cur ?next))) 
   )

  (:action pickUpFood
    :parameters (?v - vehicle ?k - kitchen ?c - customer ?k_node - node)
    :precondition (and (location_V ?v ?k_node) (location_K ?k ?k_node) (standBy ?v) (K_HasFood_C ?k ?c))
    :effect (and (not (standBy ?v)) (V_HasFood_C ?v ?c) (not (K_HasFood_C ?k ?c)))
   )  
   
  (:action deliverFood
    :parameters (?v - vehicle  ?c - customer ?c_node - node)
    :precondition (and (location_V ?v ?c_node) (location_C ?c ?c_node) (V_HasFood_C ?v ?c))
    :effect (and (standBy ?v) (not (V_HasFood_C ?v ?c)) (delivered ?c))
   )
   
 
 )