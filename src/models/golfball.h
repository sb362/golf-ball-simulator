#ifndef GOLFBALL_H
#define GOLFBALL_H

#include <QtGlobal> // qreal
#include <QtMath> // M_PI


class Golfball
{
public:
	Golfball(qreal mass, qreal radius);

	virtual ~Golfball();

	qreal mass() const;
	qreal radius() const;

	virtual qreal area() const = 0;

private:
	qreal m_mass, m_radius;
};

#endif // GOLFBALL_H
