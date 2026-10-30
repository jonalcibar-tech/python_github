def test(function):
    print(f"\n=== Testing {function} ===")
    try:
        # Import your exercise file
        # This is like doing: import ft_plot_area
        ft_module = __import__(function)

        # Get the function from your file
        # This is like doing: ft_plot_area.ft_plot_area
        ft_function = getattr(ft_module, function)

        # Special handling for ft_seed_inventory (Exercise 7)
        # This function takes parameters, unlike the others
        if function == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            # Test with packets
            ft_function("tomato", 15, "packets")
            # Test with grams
            ft_function("carrot", 8, "grams")
            # Test with area
            ft_function("lettuce", 12, "area")
            # Test with unknown unit
            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            # Run your function normally (no parameters)
            ft_function()

    except ImportError:
        print(f"❌ Could not find {function}.py")
        print(
           """   Make sure your file exists and is in the same
                folder as main.py"""
            )

    except AttributeError:
        print(f"❌ Could not find function {function}() in your file")
        print(f"   Make sure you have: def {function}():")

    except TypeError as error:
        msg = str(error)
        if "missing" in msg and "required positional argument" in msg:

            print(f"❌ Function signature error: {error}")
            print(
                """   For exercise 7, make sure your
                function takes parameters:"""
            )
            print(
                f"   def {function}"
                "(seed_type: str, quantity: int, unit: str) -> None:"
            )
        else:
            print(f"❌ Type error: {error}")
            print("   Check your function parameters and types")

    except Exception as error:
        print(f"❌ Error running your function: {error}")
        print("   Check your code for syntax errors")


def main():
    function = input("Nombre de función a testar EXcluyendo .py: ")
    test(function)


if __name__ == "__main__":
    main()
