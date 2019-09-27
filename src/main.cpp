
#include <QApplication>
#include <QCommandLineParser>
#include <QCommandLineOption>

#include "ui/mainwindow.h"


int main(int argc, char *argv[])
{
	QApplication app(argc, argv);
	QCoreApplication::setApplicationName("Golf Ball Simulator");
	QCoreApplication::setApplicationVersion("2019-09-27");

	QCommandLineParser parser;
	parser.setApplicationDescription("Simulates the flight path of a golf ball.");
	parser.addHelpOption();
	parser.addVersionOption();
	parser.process(app);

	MainWindow mainWindow;
	mainWindow.show();

	return app.exec();
}
