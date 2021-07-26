#if !defined(HAMMING_H)
#define HAMMING_H

#include <string>
#include <algorithm>
#include <stdexcept>

namespace hamming 
{
    std::size_t compute(const std::string& first_strand, 
                        const std::string& second_strand);
}

#endif // HAMMING_H
