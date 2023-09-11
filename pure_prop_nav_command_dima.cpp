#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>

namespace math {
    template <typename T>
    struct real2 {
        T x, y;
        // Define squared_length() member function here--????
        T squared_length() const {
            return x * x + y * y;// ???Is it right count?
        }
        // Define subtraction operator for math::real2
        real2 operator-(const real2& other) const {
            return {x - other.x, y - other.y};
        }
    };
}

template < typename RealType >
constexpr inline auto const pure_proportional_navigation_command(
    math::real2 < RealType > const& line_of_sight,
    math::real2 < RealType > const& target_velocity,
    math::real2 < RealType > const& interceptor_velocity,
    RealType const& effective_navigation_ratio
)
{
    auto const& line_of_sight_squared_length( line_of_sight.squared_length() );
    if ( line_of_sight_squared_length < RealType{ 1e-12 } )
        return math::real2 < RealType >{ 0 };
    
    return
        (effective_navigation_ratio *((target_velocity - interceptor_velocity)^line_of_sight)/line_of_sight_squared_length)
        * math::real2 < RealType >{ -interceptor_velocity.y, interceptor_velocity.x };
};

int main() {
    // Создаем объекты типа math::real2
    math::real2<double> line_of_sight{1.0, 2.0};
    math::real2<double> target_velocity{3.0, 4.0};
    math::real2<double> interceptor_velocity{0.5, 0.5};
    double effective_navigation_ratio = 0.1;

    // Вызываем функцию pure_proportional_navigation_command
    auto result = pure_proportional_navigation_command(line_of_sight, target_velocity, interceptor_velocity, effective_navigation_ratio);

    // Выводим результат
    std::cout << "Результат: (" << result.x << ", " << result.y << ")" << std::endl;

    return 0;
}