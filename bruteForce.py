class MinDist:
        
    def bruteForce(self,graph_nodes,dict_air):
        #transform nodes(keys) of dict into a list
        graph_nodes = (list(dict_air.keys()))
        print(graph_nodes)

        airports_visited = []
        min_dist = []
        airIndices = []
        new_source = graph_nodes[0]
        # airIndices.append(0)
        for s in graph_nodes:
            # print("Destination:", new_source)
            airports_visited.append(new_source)
            distances = dict_air.get(new_source)
            for i in airIndices:
                # print(s)
                distances[i] = 9999999
            #print(distances)
            index=-1
            for i,element in enumerate(distances):
                if element == 0: 
                    index=i
                    distances[i] = 9999999
            airIndices.append(index)
            mDist = min(distances)
            #print(mDist)
            airpIndex = distances.index(mDist)
            airIndices.append(airpIndex)
            #print("Index:",airpIndex)
            new_source = graph_nodes[airpIndex]
            min_dist.append(min(distances))
            #print(min_dist)
            #remove last element in list which is 9999999
            #min_dist = min_dist[:-1]
        return("Shortest path:", min_dist, "Airports visited:", airports_visited)

