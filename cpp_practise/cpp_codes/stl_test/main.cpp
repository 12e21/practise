#include <iostream>
#include "list"
#include "iterator"
int main() {
    std::list<int> my_array{1,1};
    //std::insert_iterator<std::list<int>> insert(my_array,++my_array.begin());
    auto insert= std::inserter(my_array,++my_array.begin());
    insert=2;
    insert=2;
    insert=2;
    for(auto val=my_array.cbegin();val!=my_array.cend();val++)
    {
        std::cout<<*val<<" ";
    }
}
