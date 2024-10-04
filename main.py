import time
import mesop as me

@me.stateclass
class State:
  input: str
  output: str
  is_open: bool = False
  gemini_api_key: str = ""

@me.page(path="/")
def page():
  dialog_box()
  with me.box(
    style=me.Style(
      background="#fff",
      min_height="calc(100% - 48px)",
    )
  ):
    with me.box(
      style=me.Style(
        width="min(720px, 100%)",
        margin=me.Margin.symmetric(horizontal=75, vertical=36),
      )
    ):
      header()
      prompt_box()
      output()
  footer()

@me.content_component
def dialog(is_open: bool):
  """Renders a dialog component.

  Args:
    is_open: Whether the dialog is visible or not.
  """
  with me.box(
    style=me.Style(
      display="block" if is_open else "none",
      margin=me.Margin.symmetric(horizontal=500, vertical=76),
      height="100%",
      position="fixed",
      width="100%",
    )
  ):
    with me.box(
      style=me.Style(
        place_items="center",
        display="grid",
        height="90vh",
      )
    ):
      with me.box(
        style=me.Style(
          background=me.theme_var("surface-container-lowest"),
          border_radius=20,
          box_sizing="content-box",
          box_shadow=(
            "0 3px 1px -2px #0003, 0 2px 2px #00000024, 0 1px 5px #0000001f"
          ),

          padding=me.Padding.all(20),
        )
      ):
        me.slot()

def header():
  with me.box(
    style=me.Style(
      padding=me.Padding(
        top=24,
        bottom=36,
      ),
    )
  ):
    me.text(
      "Meal Genie",
      style=me.Style(
        font_size=36,
        font_weight=700,
        background="linear-gradient(90deg, #4285F4, #AA5CDB, #DB4437) text",
        color="transparent",
      ),
    )

def prompt_box():
  state = me.state(State)
  with me.box(
    style=me.Style(
      border_radius=16,
      padding=me.Padding.all(8),
      background="white",
      display="flex",
      width="100%",
    )
  ):
    with me.box(style=me.Style(flex_grow=1)):
      me.native_textarea(
        value=state.input,
        placeholder="Enter your ingredients here for a delicious recipe...",
        style=me.Style(
          padding=me.Padding(top=16, left=16),
          width="100%",
          height=150,
          border=me.Border.all(me.BorderSide(width=1, style="solid")),
          ),
          on_blur=textarea_on_blur,
        )
    with me.content_button(type="icon", on_click=click_input_box):
      me.icon("send")

def textarea_on_blur(e: me.InputBlurEvent):
  state = me.state(State)
  state.input = e.value

def click_input_box(e: me.ClickEvent):
  state = me.state(State)
  state.in_progress = True
  input = state.input
  state.input = ""
  yield

  for chunk in call_api(input):
    state.output += chunk
    yield
  state.in_progress = False
  yield

def call_api(input):
  # Replace this with an actual API call
  time.sleep(0.5)
  yield "Example of streaming an output"
  time.sleep(1)
  yield "\n\nOutput: " + input

def set_gemini_api_key(e: me.InputBlurEvent):
    me.state(State).gemini_api_key = e.value

def dialog_box():
  state = me.state(State)

  with dialog(state.is_open):
    with me.box(style=me.Style(display="flex", flex_direction="column")):
        me.input(
            label="Gemini API Key",
            value=state.gemini_api_key,
            on_blur=set_gemini_api_key,
        )
        me.button("Confirm", on_click=on_click_close_dialog)

def output():
  state = me.state(State)
  if state.output:
    with me.box(
      style=me.Style(
        background="#F0F4F9",
        padding=me.Padding.all(16),
        border_radius=16,
        margin=me.Margin(top=36),
      )
    ):
      if state.output:
        me.markdown(state.output)

def footer():
  with me.box(
    style=me.Style(
      display="flex", flex_direction="row",
      position="sticky",
      bottom=0,
      padding=me.Padding.symmetric(vertical=16, horizontal=16),
      width="100%",
      background="#F0F4F9",
      font_size=14,
    )
  ):
    with me.box(style=me.Style(width="90%")):
      me.html(
        "Made with <a href='https://google.github.io/mesop/'>Mesop</a>",
      )
    with me.box(style=me.Style(width="10%")):
      me.button("API Key", type="stroked", color="primary", on_click=on_click_open_dialog)

def on_click_close_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = False


def on_click_open_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = True

