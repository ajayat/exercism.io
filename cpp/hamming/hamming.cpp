#include "hamming.h"

namespace hamming 
{
    std::size_t compute(const std::string& first_strand, 
                        const std::string& second_strand) 
    {
        if (first_strand.size() != second_strand.size())
            throw std::domain_error("Strands are not of equal length.");

        std::size_t hamming_distance = 0;
        for (std::size_t i = 0; i < first_strand.size(); ++i) 
        {
            if (first_strand[i] != second_strand[i])
                ++hamming_distance;
        }
        return hamming_distance;
    }
}  // namespace hamming
