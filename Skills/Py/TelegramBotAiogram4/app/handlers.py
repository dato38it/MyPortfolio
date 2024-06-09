from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
import app.database.requests as rq
router = Router()
'''
class Register(StatesGroup):
    name = State()
    age = State()
    number = State()
'''
#@router.message()
@router.message(CommandStart())
async def cmd_start(message: Message):
    #await message.answer('Hey!')
    #await message.answer('Hey!', reply_markup=kb.main)
    #await message.reply('How are you')
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в магазин кроссовок!', reply_markup=kb.main)
'''
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('You clicked helps button')
#@router.message(F.text == 'Im ok')
#async def nice(message: Message):
#    await message.answer('Its cool')
@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорю', reply_markup=kb.catalog)
@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию', show_alert=True)
    await callback.message.answer('Вы выбрали категорию футболок')
@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя:')
@router.message(Register.name)
async def register(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваше возраст:')
@router.message(Register.age)
async def register(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Введите ваше номер телефона:', reply_markup=kb.get_number)
@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data= await state.get_data()
    await message.answer(f'Your name: {data["name"]}\nYour age: {data["age"]}\nYour number: {data["number"]}')
    await state.clear()
'''
@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорю товара', reply_markup=await kb.categories())
@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории', 
                                  reply_markup=await kb.items(callback.data.split('_')[1]))
@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Навзвание: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$', 
                                  reply_markup=await kb.items(callback.data.split('_')[1]))
