from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton, QRadioButton,
    QVBoxLayout, QHBoxLayout,
    QGroupBox, QButtonGroup
)  
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Какого СССР-го пилота звали грозой немцев?', 'Покрышкин', 'Колобанов', 'Сталин', 'Ельцин'))
question_list.append(Question('Кто уничтожал одиночные, важные цели во время WW2?', 'Снайперы', 'Танкисты', 'Лётчики', 'Пехота'))
question_list.append(Question('На каком танке Калабанов совершил подвиг?', 'КВ-1', 'Т-34', 'ИС', 'Т-50'))

app = QApplication([])
winn = QWidget()
winn.setWindowTitle('WW2 Вопросы')
winn.resize(500, 400)

question = QLabel('На каком танке Калабанов совершил подвиг?')
answer = QPushButton('Ответить')


RadioGroupBox = QGroupBox("Варианты ответов:")
but1 = QRadioButton('КВ 2')
but2 = QRadioButton('КВ 1')
but3 = QRadioButton('Т 34')
but4 = QRadioButton('ИС')

RadioGroup = QButtonGroup()
RadioGroup.addButton(but2)
RadioGroup.addButton(but1)
RadioGroup.addButton(but3)
RadioGroup.addButton(but4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Правильно/Неправильно')
lb_corect = QLabel('ответ будет тут!')

l_res = QVBoxLayout()
l_res.addWidget(lb_result, alignment=(Qt.AlignHCenter |  Qt.AlignVCenter))
l_res.addWidget(lb_corect, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(l_res)



layout_ans2.addWidget(but1)
layout_ans2.addWidget(but2)
layout_ans3.addWidget(but3)
layout_ans3.addWidget(but4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()

layout_l1.addWidget(question, alignment=(Qt.AlignHCenter |  Qt.AlignVCenter))
layout_l2.addWidget(RadioGroupBox)
layout_l2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_l3.addStretch(1)
layout_l3.addWidget(answer, stretch=2)
layout_l3.addStretch(1)

l_card = QVBoxLayout()
l_card.addLayout(layout_l1, stretch=2)
l_card.addLayout(layout_l2, stretch=8)
l_card.addStretch(1)
l_card.addLayout(layout_l3, stretch=1)
l_card.addStretch(1)
l_card.setSpacing(5)

winn.setLayout(l_card)

#Функции
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')

def show_qestion():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    but1.setChecked(False)
    but2.setChecked(False)
    but3.setChecked(False)
    but4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if 'Ответить' == answer.text():
        show_result()
    else:
        show_qestion()

an = [but1, but2, but3, but4]
def ask(q):
    shuffle(an)
    an[0].setText(q.right_answer)
    an[1].setText(q.wrong1)
    an[2].setText(q.wrong2)
    an[3].setText(q.wrong3)
    question.setText(q.question)
    lb_corect.setText(q.right_answer)
    show_qestion()


def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if an[0].isChecked():
        show_correct('Правильно!')
        winn.score += 1
        print('Статистика\n-Всего вопросов: ', winn.total, '\n-Правильных ответов: ', winn.score)
        print('Рейтинг: ', (winn.score/winn.total*100), '%')
    else:
        if an[1].isChecked() or an[2].isChecked() or an[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг: ', (winn.score/winn.total*100), '%')

def next_qestion():
    cur_quest =  randint(0, len(question_list)-1)
    winn.total += 1
    print('Статистика\n-Всего вопросов: ', winn.total, '\n-Правильных ответов: ', winn.score)
    q = question_list[cur_quest]
    ask(q)

def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_qestion()

answer.clicked.connect(click_OK)

winn.score = 0
winn.total = 0
next_qestion()


winn.show()
app.exec_()
