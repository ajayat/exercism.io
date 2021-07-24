#if !defined(HAMMING_H)
#define HAMMING_H

#include <string>
#include <algorithm>
#include <stdexcept>

namespace hamming 
{
    int compute(std::string first_strand, std::string second_strand);
}

#endif // HAMMING_H
