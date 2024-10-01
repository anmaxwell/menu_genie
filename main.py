import mesop as me

@me.stateclass
class State:
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
        placeholder="Enter your ingredients here for a delicious recipe...",
        style=me.Style(
          padding=me.Padding(top=16, left=16),
          width="100%",
          height=150,
          border=me.Border.all(me.BorderSide(width=1, style="solid")),
          ),
        )
    with me.content_button(type="icon", on_click=navigate):
      me.icon("send")

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

def footer():
  with me.box(
    style=me.Style(
      position="sticky",
      bottom=0,
      padding=me.Padding.symmetric(vertical=16, horizontal=16),
      width="100%",
      background="#F0F4F9",
      font_size=14,
    )
  ):
    me.html(
      "Made with <a href='https://google.github.io/mesop/'>Mesop</a>",
    )
    with me.box(
     style=me.Style(
        display="flex",
        flex_direction="row",
        justify_content="right")
    ):
     me.button("API Key", type="stroked", color="primary", on_click=on_click_open_dialog)

def on_click_close_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = False


def on_click_open_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = True

def navigate(event: me.ClickEvent):
  me.navigate("/about")

@me.page(path="/about")
def page():
  with me.box(style=me.Style(display="flex", flex_direction="row")):
    with me.box(style=me.Style(background="red", height=50, width="75%")):
      me.text("test text")
    with me.box(style=me.Style(background="blue", height=100, width="25%")):
      me.text("second test",
      style=me.Style(
        font_size=36,
        font_weight=700,
        background="linear-gradient(90deg, #4285F4, #AA5CDB, #DB4437) text",
        color="transparent",
        text_align="right"
      ),)
