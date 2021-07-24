#if !defined(LEAP_H)
#define LEAP_H

namespace leap 
{
    // paramaters must be signed for arithmetic
    // https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Res-mix
    bool is_leap_year(int year);
}  // namespace leap

#endif // LEAP_H
