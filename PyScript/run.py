import GenerateData
import OnlineSolver

customerLimit = 20
KitchenLimit=5
deliveryboyLImit=3
nodeDulication=1


if __name__ == "__main__":
    GenerateData.Generate(customerLimit,KitchenLimit,deliveryboyLImit,nodeDulication)
    OnlineSolver.Solve()
    input("Press Enter to continue...")

    

