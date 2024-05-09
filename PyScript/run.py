import GenerateData
import OnlineSolver

customerLimit = 15
KitchenLimit=6
deliveryboyLImit=5
nodeDulication=5


if __name__ == "__main__":
    GenerateData.Generate(customerLimit,KitchenLimit,deliveryboyLImit,nodeDulication)
    OnlineSolver.Solve()
    input("Press Enter to continue...")
    

