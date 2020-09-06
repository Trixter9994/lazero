import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
from polygon import RatotionPoly
from sequence import getData,getConvex,BottomLeftFill
import time
import multiprocessing
import datetime

class GA(object):
    '''
    参考文献：
    '''
    def __init__(self,poly_list):
        '''
        种群的大小 pop_size
        选择个数 elite_size
        每个位置的变异概率(方向或位置交换) mutate_rate
        总的繁殖代数 generations
        ''' 
        self.elite_size=5
        self.mutate_rate=0.1
        self.generations=10
        self.ratotionPoly=RatotionPoly(360)
        self.pop_size=10
        self.poly_list=poly_list
        self.fitness_record=[]
        self.sequence_record=[]
        print("共",len(poly_list),"个形状")
        print("一代",self.pop_size,"个序列")
        print("每代选择",self.elite_size,"个序列")
        print("变异概率",self.mutate_rate)
        print("共",self.generations,"代")

        print("执行程序")
        self.geneticAlgorithm()
        # self.geneticAlgorithmPlot()

        print("最佳序列/位置:")
        print(self.best_sequence)

    # 创建一个序列
    def createSequence(self):
        sequence = random.sample(self.poly_list, len(self.poly_list))
        return sequence

    # 初始化种群
    def initialPopulation(self):
        self.pop = []
        for i in range(0, self.pop_size):
            self.pop.append(self.createSequence()) # 生成随机序列

    def deleteRedundancy(self,_arr):
        new_arr = []
        for item in _arr:
            if not item in new_arr:
                new_arr.append(item)
        return new_arr
    
    def addNewRecord(self,fitness_results):
        for result in fitness_results:
            if result[2] not in self.sequence_record:
                self.fitness_record.append(result[1])
                self.sequence_record.append(result[2])
    
    def getIndex(self,seq):
        for i,record in enumerate(self.sequence_record):
            if seq==record:
                print("在",i,"位置上")
                return i
            # else:
            #     print("seq:",seq)
            #     print("record:",record)
        return -1

    # 对序列进行排序
    def rankSequences(self,population):
        multi=True
        fitness_results = []
        target_seq=[]
        cores = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes=cores)
        if multi==True:
            print("共有",len(population),"个")
            new_population=[]
            for i in range(0,len(population)):
                record_index=self.getIndex(population[i])
                if record_index>=0:
                    fitness_results.append([i,self.fitness_record[self.sequence_record.index(population[i])],population[i]])
                else:
                    new_population.append(population[i])
                    fitness_results.append([i,0,population[i]])
            new_population=self.deleteRedundancy(new_population) # 删除冗余
            print("该代共需要计算",len(new_population),"次")
            tasks=[[pop] for pop in new_population]
            results=pool.starmap(self.fitness,tasks)
            # 将计算结果填充进去
            for j,seq in enumerate(new_population):
                for item in fitness_results:
                    if item[2]==seq:
                        item[1]=results[j]
            self.addNewRecord(fitness_results)
        else:
            for i in range(0,len(population)):
                fitness_results[i] = self.fitness(population[i]) # index和fitness共同排序

        self.current_pop_ranked=sorted(fitness_results, key = operator.itemgetter(1), reverse = True) # 排序，包含index

    # 适配程度，用于进化选择
    def fitness(self,sequence):
        pp=BottomLeftFill(1500,sequence)
        fitness=1000/float(pp.contain_height) # 选择倒数
        return fitness
    
    # 根据排序选择序列
    def selection(self):
        pop_ranked= self.current_pop_ranked
        selection_results = []
        df = pd.DataFrame(np.array(pop_ranked), columns=["index","fitness","seq"])
        df['cum_sum'] = df.fitness.cumsum() # 计算累加值
        df['cum_perc'] = 100*df.cum_sum/df.fitness.sum() # 计算百分比

        # 选择出排在前面的几个序列
        for i in range(0, self.elite_size):
            selection_results.append(pop_ranked[i][0])
        # 缺少的序列用已有的序列补上
        for i in range(0, len(pop_ranked) - self.elite_size):
            pick = 100*random.random()
            for i in range(0, len(pop_ranked)):
                if pick <= df.iat[i,3]:
                    selection_results.append(pop_ranked[i][0])
                    break
        return selection_results

    # 获得matingPool用于繁殖
    def matingPool(self,population, selection_results):
        mating_pool = []
        for i in range(0, len(selection_results)):
            index = selection_results[i]
            mating_pool.append(population[index])
        return mating_pool

    # 序列交配修改顺序（不修改方向）
    def breed(self,parent1, parent2):
        child = []
        childP1 = []
        childP2 = []
    
        # 选择截取的范围
        geneA = int(random.random() * len(parent1))
        geneB = int(random.random() * len(parent1))
    
        start_gene = min(geneA, geneB)
        end_gene = max(geneA, geneB)

        for i in range(start_gene, end_gene):
            childP1.append(parent1[i])
        
        childP2 = [item for item in parent2 if item not in childP1]

        child = childP1 + childP2
        return child

    # 繁殖种群，输入pool和size
    def breedPopulation(self,mating_pool):
        children = []
        length = len(mating_pool) - self.elite_size
        pool = random.sample(mating_pool, len(mating_pool))

        for i in range(0,self.elite_size):
            children.append(mating_pool[i])
    
        for i in range(0, length):
            child = self.breed(pool[i], pool[len(mating_pool)-i-1])
            children.append(child)
        return children

    # 个体突变，随机交换或方向改变
    def mutate(self,individual):
        for swapped in range(len(individual)):
            if(random.random() < self.mutate_rate):
                # 首先是交换位置
                if random.random()<=0.5:
                    swapWith = int(random.random() * len(individual))
            
                    poly1 = individual[swapped]
                    poly2 = individual[swapWith]
            
                    individual[swapped] = poly1
                    individual[swapWith] = poly2
                else:
                    index = random.randint(0,len(individual)-1)
                    self.ratotionPoly.rotation(individual[index])
        return individual

    # 种群突变
    def mutatePopulation(self,population):
        mutated_pop = []
    
        for ind in range(0, len(population)):
            mutated_ind = self.mutate(population[ind])
            mutated_pop.append(mutated_ind)

        return mutated_pop

    # 获得下一个形状
    def nextGeneration(self):
        self.rankSequences(self.pop) # 获得子代
        print("Fitness : ",str(self.current_pop_ranked[0][1]))
        selection_results = self.selection()
        mating_pool = self.matingPool(self.pop, selection_results)
        children = self.breedPopulation(mating_pool)
        self.pop = self.mutatePopulation(children)

    # GA算法核心步骤
    def geneticAlgorithm(self):
        self.initialPopulation() # 生成随机序列

        # 持续获得下一代
        for i in range(0, self.generations):
            print("############################计算第",i+1,"代#######################################")
            self.nextGeneration() 
    
        print("Final fitness: " + str(self.current_pop_ranked[0][1]))
        best_index = self.current_pop_ranked[0][0]
        self.best_sequence = self.pop[best_index]

    # 带打点的函数
    def geneticAlgorithmPlot(self):
        self.initialPopulation()
        progress = []
        self.rankSequences(self.pop)
        progress.append(1000 / self.current_pop_ranked[0][1]) # 存储最好的情况
    
        for i in range(0, self.generations):
            print("############################计算第",i+1,"代#######################################")
            self.nextGeneration()
            progress.append(1000 / self.current_pop_ranked[0][1])
    
        best_index = self.current_pop_ranked[0][0]
        self.best_sequence = self.pop[best_index]

        plt.plot(progress)
        plt.ylabel('Height')
        plt.xlabel('Generation')
        plt.show()

if __name__=='__main__':
    starttime = datetime.datetime.now()
    GA(getConvex())
    # BottomLeftFill(1500,getData())
    endtime = datetime.datetime.now()
    print (endtime - starttime)