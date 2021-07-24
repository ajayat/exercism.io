#include "hamming.h"

namespace hamming 
{
    int compute(std::string first_strand, std::string second_strand) 
    {
        if (first_strand.size() != second_strand.size())
            throw std::domain_error("Strands are not of equal length.");

        int hamming_distance = 0;
        for (int i = 0; i < static_cast<int>(first_strand.size()); ++i) 
        {
            if (first_strand[i] != second_strand[i])
                ++hamming_distance;
        }
        return hamming_distance;
    }
}  // namespace hamming
