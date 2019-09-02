class Node:
    def __init__(self):
        self.m_children_nodes={}
        self.m_total_word_so_far=''
        self.m_current_letter=''
        self.m_word=''
        self.m_curr_index=0
        self.is_end=0
        self.word_list = []


    def add_word(self,word, index_in_list, word_so_far='',curr_index=-1):
        self.m_word=word
        self.m_curr_index=curr_index

        if self.m_curr_index>=0:
            self.m_current_letter=self.m_word[self.m_curr_index]
            self.m_total_word_so_far=word_so_far+self.m_word[self.m_curr_index]
            if(self.m_curr_index==len(self.m_word)-1):
                self.is_end = 1
                self.word_list.append(index_in_list)
        if self.m_curr_index+1 <len(self.m_word):                                                                                   
            next_child = self.m_word[self.m_curr_index+1]
            if next_child not in self.m_children_nodes:
                self.m_children_nodes[next_child]=Node()
            self.m_children_nodes[next_child].add_word(self.m_word,index_in_list, self.m_total_word_so_far,self.m_curr_index+1)
    def auto_complete_word(self,str):
        result = []
        if len(str)>0 and str[0] in self.m_children_nodes:
            result = self.m_children_nodes[str[0]].auto_complete_word(str[1:])
        if len(str)==0:
            #print("auto-complete:")
            result = self.return_tree()
            #self.word_list
        return result
    def return_tree(self):
        result=[]
        if self:
            if self.is_end==1:
                for i in self.word_list:
                    result.append(i)
            for i in self.m_children_nodes:
                result = result + self.m_children_nodes[i].return_tree()
        return result 
    def print_tree(self):
        if self:
            if self.is_end==1:
                print('word: ',self.m_total_word_so_far)
                print("Indexes : ", str(self.word_list))
            for i in self.m_children_nodes:
                self.m_children_nodes[i].print_tree()
