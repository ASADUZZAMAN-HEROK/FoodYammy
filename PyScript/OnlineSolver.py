import requests
import time
from pprint import pprint
import json


def Solve():

    req_body = {
    "domain":"(define (domain BLOCKS) (:requirements :strips) (:predicates (on ?x ?y) (ontable ?x) (clear ?x) (handempty) (holding ?x) ) (:action pick-up :parameters (?x) :precondition (and (clear ?x) (ontable ?x) (handempty)) :effect (and (not (ontable ?x)) (not (clear ?x)) (not (handempty)) (holding ?x))) (:action put-down :parameters (?x) :precondition (holding ?x) :effect (and (not (holding ?x)) (clear ?x) (handempty) (ontable ?x))) (:action stack :parameters (?x ?y) :precondition (and (holding ?x) (clear ?y)) :effect (and (not (holding ?x)) (not (clear ?y)) (clear ?x) (handempty) (on ?x ?y))) (:action unstack :parameters (?x ?y) :precondition (and (on ?x ?y) (clear ?x) (handempty)) :effect (and (holding ?x) (clear ?y) (not (clear ?x)) (not (handempty)) (not (on ?x ?y)))))",
    "problem":"(define (problem BLOCKS-4-0) (:domain BLOCKS) (:objects D B A C ) (:INIT (CLEAR C) (CLEAR A) (CLEAR B) (CLEAR D) (ONTABLE C) (ONTABLE A) (ONTABLE B) (ONTABLE D) (HANDEMPTY)) (:goal (AND (ON D C) (ON C B) (ON B A))) )"
    }

    with open("../PDDL/FoodYammyDomain.pddl", "r") as f:
        req_body["domain"]=f.read()
        f.close()

    with open("../PDDL/FoodYammyProblem.pddl", "r") as f:
        req_body["problem"]=f.read()
        f.close()

    # Send job request to solve endpoint
    solve_request_url=requests.post("https://solver.planning.domains:5001/package/dual-bfws-ffparser/solve", json=req_body).json()


    print('Computing...')
    # Query the result in the job
    celery_result=requests.post('https://solver.planning.domains:5001' + solve_request_url['result'])

    print('Computing...')
    while celery_result.json().get("status","")== 'PENDING':
        print('Computing...')
        # Query the result every 0.5 seconds while the job is executing
        celery_result=requests.post('https://solver.planning.domains:5001' + solve_request_url['result'])
        time.sleep(0.5)

    pprint(celery_result.json())
    with open("../Result/PlanningResult.json", "w") as f:
        json.dump(celery_result.json(),f)
    return celery_result