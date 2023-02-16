#include <iostream>
#include <pthread.h>
#include <unistd.h>
template <typename type_1>
void* print(void* print_text_p)
{
    type_1 print_text;
    print_text=*((type_1*)print_text_p);
    while(1)
    {
        std::cout<<print_text<< std::endl;
        sleep(1);
    }
}

int main() {
    pthread_t wish_1;
    int text_1 = 3;
    pthread_create(&wish_1, NULL, print<int>, (void *) &text_1);
    pthread_exit(NULL);
}

