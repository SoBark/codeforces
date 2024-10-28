#include <iostream>

#define F {std::cout << __PRETTY_FUNCTION__ << "\n";}

#include <vector>
#include <iterator>
#include <algorithm>

struct A
{
    int* a = new int(5);

    A() { std::cout << __PRETTY_FUNCTION__ << "\n"; }

    ~A() { delete a; a = nullptr; std::cout << __PRETTY_FUNCTION__ << "\n"; }
    A(const A&) { std::cout << __PRETTY_FUNCTION__ << "\n"; }
    A(A&& f) { std::cout << __PRETTY_FUNCTION__ << "\n"; delete a; a = f.a; f.a = nullptr; }

    A& operator=(const A&) { std::cout << __PRETTY_FUNCTION__ << "\n"; return *this; }
    A& operator=(A&&) { std::cout << __PRETTY_FUNCTION__ << "\n"; return *this; }
};

std::ostream& operator<<(std::ostream& os, const A& a)
{
    return os << a.a;
}

void print()
{
}

template<typename T, typename... Args>
void print(T&& a, Args&&... args)
{
    using Type = std::decay<decltype(*a.begin())>::type;

    std::copy(a.begin(), a.end(), std::ostream_iterator<Type>(std::cout, " "));
    std::cout << "\n";
    print(args...);
}

int main()
{
    A a1, a2, a3, a4, a5, a6;
    std::cout << "1\n";
    std::vector<A> a{ a1, a2, a3 }, b{ a4, a5, a6 };
    std::cout << "2\n";
    a = std::move(b);

    std::cout << *a[0].a;

    std::cout << "3\n";

    print(a, b);

    std::cout << "4\n";

    return 0;
}