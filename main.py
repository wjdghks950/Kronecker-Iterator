import argparse
from Kronecker import KProds
from Analysis import Analysis
import time

if __name__ == "__main__":

    # Parse the arguments
    parser = argparse.ArgumentParser(description="Generating kronecker graphs")
    parser.add_argument(
        "-f",
        "--fileName",
        action="store",
        default="A.txt",
        type=str,
        help="A file name for an initial matrix",
    )
    parser.add_argument(
        "-k",
        "--k",
        action="store",
        default=13,
        type=int,
        help="The number of Kroncker products",
    )
    parser.add_argument(
        "-o",
        "--outputName",
        action="store",
        default="A.png",
        type=str,
        help="A file name for an output matrix",
    )
    args = parser.parse_args()

    start = time.time()
    # Initialize the kronecker object
    kprods: KProds = KProds(k = args.k, filePath=args.fileName)

    # Generate Kronecker graphs
    adj = kprods.produceGraph()

    # Analyze the graph
    analysis: Analysis = Analysis(adj, args.outputName)
    end = time.time()
    print(end - start)
    analysis.plotDegDist()